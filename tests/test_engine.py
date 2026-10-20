import pytest
from datetime import date, timedelta
from central_bank_engine_v13 import (
    CentralBankGame,
    Decision,
    RepoPosition,
    SecuritySlice,
)

START = date(2025, 1, 1)

def game(**kwargs):
    return CentralBankGame(start_date=START, initial_interbank_rate=3.95, seed=17, **kwargs)

def decision(
    action="Buy Securities",
    volume=0,
    enabled=True,
    expected=None,
):
    return Decision(
        auction_method="Interest-rate auction",
        omo_action=action,
        volume=volume,
        pricing_method="Single-price",
        expected_inflation=expected,
        auction_enabled=enabled,
    )

def test_interest_rate_auction_accepts_valid_decision():
    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=1000,
        pricing_method="Single-price",
    )
    decision.validate()
    assert decision.volume == 1000
    assert decision.pricing_method == "Single-price"
    assert decision.repo_rate is None


def test_negative_volume_is_rejected():
    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=-100,
        pricing_method="Single-price",
    )
    with pytest.raises(ValueError, match="Volume must be >= 0"):
        decision.validate()


def test_volume_auction_requires_an_auction_rate():
    decision = Decision(
        auction_method="Volume auction",
        omo_action="Repo",
        volume=1000,
        repo_rate=None,
    )
    with pytest.raises(
        ValueError,
        match="requires the user-entered auction rate",
    ):
        decision.validate()


def test_volume_auction_rejects_rate_above_limit():
    decision = Decision(
        auction_method="Volume auction",
        omo_action="Repo",
        volume=1000,
        repo_rate=10.5,
    )
    with pytest.raises(ValueError, match="between 0 and 10"):
        decision.validate()


def test_game_initializes_with_initial_interbank_rate():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )
    assert game.phase == 1
    assert game.interbank_rate == 3.95


def test_phase_one_requires_expected_inflation():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )
    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=None,
        auction_enabled=False,
    )
    with pytest.raises(ValueError, match="requires Expected Inflation"):
        game.run_phase(4000, decision)


def test_liquidity_gap_and_interbank_rate_without_auction():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )
    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=4.0,
        auction_enabled=False,
    )
    result = game.run_phase(4000, decision)

    # Phase 1 scenario demand is 4,000; no auction or maturities.
    assert result.scenario_liquidity_demand == 4000.0
    assert result.supply == 0.0
    assert result.maturity_volume == 0.0
    assert result.liquidity_gap == 4000.0

    # Interbank Formula
    assert result.interbank_rate == 4.35

    # Macro results are calculated but not published before Phase 3.
    assert result.gdp_growth is None
    assert result.inflation is None


def test_macro_results_are_published_every_three_phases():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    # Phase 1: nhập Expected Inflation cho chu kỳ 3 phase.
    phase1_decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=4.0,
        auction_enabled=False,
    )

    result1 = game.run_phase(4000, phase1_decision)

    assert result1.phase == 1
    assert result1.expected_inflation is None
    assert result1.gdp_growth is None
    assert result1.inflation is None
    assert game.phase == 2

    # Phase 2: chưa công bố kết quả kinh tế vĩ mô.
    phase2_decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=None,
        auction_enabled=False,
    )

    result2 = game.run_phase(4000, phase2_decision)

    assert result2.phase == 2
    assert result2.expected_inflation is None
    assert result2.gdp_growth is None
    assert result2.inflation is None
    assert game.phase == 3

    # Phase 3: công bố kết quả của chu kỳ Phase 1–3.
    phase3_decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=None,
        auction_enabled=False,
    )

    result3 = game.run_phase(4000, phase3_decision)

    assert result3.phase == 3
    assert result3.expected_inflation == 4.0
    assert result3.gdp_growth is not None
    assert result3.inflation is not None
    assert game.phase == 4

def test_interest_rate_auction_allocation_is_consistent():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Sell Securities",
        volume=1000,
        pricing_method="Single-price",
    )

    result = game.run_auction(decision, rld=4000)

    bids = result["bids"]

    assert len(bids) == 5

    allocated_volume = sum(bid.real_volume for bid in bids)

    assert allocated_volume == result["total_real_volume"]
    assert allocated_volume <= decision.volume

    for bid in bids:
        assert bid.won == (bid.real_volume > 0)

def test_single_price_auction_uses_common_settlement_rate():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Sell Securities",
        volume=1000,
        pricing_method="Single-price",
    )

    result = game.run_auction(decision, rld=4000)

    for bid in result["bids"]:
        assert bid.settlement_rate == result["win_rate"]


def test_multi_price_auction_uses_each_bid_rate():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Sell Securities",
        volume=1000,
        pricing_method="Multi-price",
    )

    result = game.run_auction(decision, rld=4000)

    for bid in result["bids"]:
        assert bid.settlement_rate == bid.bid_rate

def test_buy_securities_award_does_not_exceed_available_inventory():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=100000,
        pricing_method="Single-price",
    )

    result = game.run_auction(decision, rld=4000)

    assert result["total_real_volume"] <= result["total_bid_volume"]
    assert result["total_real_volume"] <= decision.volume


def test_volume_auction_uses_selected_rate_for_all_bids():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Volume auction",
        omo_action="Sell Securities",
        volume=1000,
        repo_rate=4.25,
    )

    result = game.run_auction(decision, rld=4000)

    assert len(result["bids"]) == 5

    for bid in result["bids"]:
        assert bid.bid_rate == 4.25
        assert bid.settlement_rate == 4.25

    assert result["win_rate"] == 4.25


def test_volume_auction_allocation_is_consistent():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Volume auction",
        omo_action="Sell Securities",
        volume=1000,
        repo_rate=4.25,
    )

    result = game.run_auction(decision, rld=4000)

    bids = result["bids"]
    allocated_volume = sum(bid.real_volume for bid in bids)

    assert len(bids) == 5
    assert allocated_volume == result["total_real_volume"]
    assert allocated_volume <= decision.volume

    for bid in bids:
        assert bid.won == (bid.real_volume > 0)



def test_sell_securities_reduces_liquidity():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Sell Securities",
        volume=1000,
        pricing_method="Single-price",
        expected_inflation=4.0,
        auction_enabled=True,
    )

    result = game.run_phase(4000, decision)

    # Selling securities absorbs liquidity, so supply is negative.
    assert result.supply < 0
    assert result.total_real_volume > 0


def test_phase_two_rejects_expected_inflation():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    # Complete Phase 1 first, because Phase 2 follows it.
    phase_one_decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=4.0,
        auction_enabled=False,
    )
    game.run_phase(4000, phase_one_decision)

    # Phase 2 should not accept Expected Inflation input.
    phase_two_decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        expected_inflation=4.0,
        auction_enabled=False,
    )
    with pytest.raises(ValueError):
        game.run_phase(4000, phase_two_decision)


def test_phase_four_requires_expected_inflation():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    for _ in range(3):
        decision = Decision(
            auction_method="Interest-rate auction",
            omo_action="Buy Securities",
            volume=0,
            pricing_method="Single-price",
            expected_inflation=(
                4.0 if game.phase == 1 else None
            ),
            auction_enabled=False,
        )
        game.run_phase(4000, decision)

    phase_four_decision = Decision(
        auction_method="Interest-rate auction",
        omo_action="Buy Securities",
        volume=0,
        pricing_method="Single-price",
        auction_enabled=False,
    )
    with pytest.raises(ValueError):
        game.run_phase(4000, phase_four_decision)


def test_macro_calculation_matches_expected_formulas():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )

    game.pending_expected_inflation = 4.0

    result = game._calculate_macro_block(interbank_rate=4.0)

    assert result["expected_inflation"] == 4.0
    assert result["real_interest_rate"] == 0.0
    assert result["output_gap"] == 0.5
    assert result["gdp_growth"] == 6.5
    assert result["inflation"] == 3.65


def test_real_rate_above_neutral_reduces_output_gap():
    game = CentralBankGame(
        start_date=date(2025, 1, 1),
        initial_interbank_rate=8.0
    )
    game.pending_expected_inflation = 4.0
    game.last_macro_output_gap = 0.0

    # Real rate = 8% - 4% = 4%, above the neutral rate of 2%.
    result = game._calculate_macro_block(interbank_rate=8.0)

    assert result["real_interest_rate"] == 4.0
    assert result["output_gap"] == -0.5


def test_real_rate_below_neutral_increases_output_gap():
    game = CentralBankGame(
        start_date=date(2025, 1, 1),
        initial_interbank_rate=4.0
    )
    game.pending_expected_inflation = 4.0
    game.last_macro_output_gap = 0.0

    # Real rate = 4% - 4% = 0%, below the neutral rate of 2%.
    result = game._calculate_macro_block(interbank_rate=4.0)

    assert result["real_interest_rate"] == 0.0
    assert result["output_gap"] == 0.5


def test_interest_rate_injection_bids_are_sorted_highest_first():
    g = game()
    g.initialize_market_tbill(face_value=20_000, rate=4.0)
    out = g.run_auction(decision(action="Buy Securities", volume=5_000), 4_000)
    rates = [b.bid_rate for b in out["bids"]]
    assert rates == sorted(rates, reverse=True)


def test_interest_rate_absorption_bids_are_sorted_lowest_first():
    g = game()
    out = g.run_auction(decision(action="Sell Securities", volume=5_000), -4_000)
    rates = [b.bid_rate for b in out["bids"]]
    assert rates == sorted(rates)

def test_buy_bid_demand_can_exceed_inventory_but_award_cannot():
    g = game()
    g.initialize_market_tbill(face_value=100, rate=4.0)
    out = g.run_auction(decision(action="Buy Securities", volume=10_000), 4_000)
    assert out["total_bid_volume"] >= out["total_real_volume"]
    assert out["total_real_volume"] <= 100
    assert g.remaining_unmatured_tbill_volume() >= 0


def test_fifo_inventory_consumes_oldest_eligible_lot_first():
    g = game()
    older = g.market_inventory.add_lot(100, START, 3.0, tenor_days=90)
    newer = g.market_inventory.add_lot(200, START + timedelta(days=1), 4.0, tenor_days=90)
    slices = g.market_inventory.take_fifo(150, START)
    assert [(s.security_id, s.face_value) for s in slices] == [
        (older.security_id, 100), (newer.security_id, 50)
    ]
    assert g.market_inventory.total_face_value(START) == 150

def test_matured_tbill_is_paid_once_and_removed_from_inventory():
    g = game()
    g.market_inventory.add_lot(750, START, 3.0, tenor_days=30)
    amount1, events1 = g.process_maturities(START + timedelta(days=30))
    amount2, events2 = g.process_maturities(START + timedelta(days=30))
    assert amount1 == 750
    assert len([e for e in events1 if e["type"] == "SBV Bill maturity"]) == 1
    assert amount2 == 0
    assert events2 == []
    assert g.remaining_unmatured_tbill_volume() == 0

@pytest.mark.parametrize(("action", "expected_sign"), [("Repo", 1), ("Reverse Repo", -1)])
def test_repo_contract_maturity_has_correct_cashflow_sign(action, expected_sign):
    g = game()
    start = START
    maturity = START + timedelta(days=60)
    g.repo_positions.append(RepoPosition(
        position_id="TEST1", bank="A", action=action,
        start_date=start, maturity_date=maturity, face_value=100,
        initial_cash=100, transaction_rate=10.0, securities=[], status="active"
    ))
    total, events = g.process_maturities(maturity)
    contract_event = next(e for e in events if e["type"] == f"{action} maturity")
    assert total * expected_sign > 0
    assert contract_event["cash_flow"] * expected_sign > 0
    assert g.repo_positions[0].status == "matured"
    assert g.process_maturities(maturity)[0] == 0


def test_disabled_auction_still_processes_phase_end_maturity_and_gap():
    g = game(phase_days=30, tbill_tenor_days=30)
    g.initialize_market_tbill(face_value=1000, rate=0.0)
    result = g.run_phase(999999, decision(enabled=False, expected=4.0))
    assert result.scenario_liquidity_demand == 4000
    assert result.supply == 0
    assert result.maturity_volume == 1000
    assert result.total_supply == 1000
    assert result.liquidity_gap == 3000
    assert result.auction_bids == []
    assert g.remaining_unmatured_tbill_volume() == 0

def test_reverse_repo_underlying_bill_matures_before_contract_without_double_count():
    g = game()
    start = START
    bill_maturity = START + timedelta(days=30)
    contract_maturity = START + timedelta(days=60)
    security = SecuritySlice(
        security_id="CBB0001", face_value=100, tbill_rate=3.0,
        issue_date=start - timedelta(days=60), maturity_date=bill_maturity
    )
    g.repo_positions.append(RepoPosition(
        position_id="RRP0001", bank="A", action="Reverse Repo",
        start_date=start, maturity_date=contract_maturity, face_value=100,
        initial_cash=100, transaction_rate=4.0, securities=[security], status="active"
    ))
    first_flow, first_events = g.process_maturities(bill_maturity)
    assert first_flow == 100
    assert len([e for e in first_events if e["type"] == "SBV Bill maturity"]) == 1
    assert security.face_value == 0
    assert g.repo_positions[0].status == "active"

    second_flow, second_events = g.process_maturities(contract_maturity)
    assert second_flow < 0
    assert len([e for e in second_events if e["type"] == "SBV Bill maturity"]) == 0
    assert len([e for e in second_events if e["type"] == "Reverse Repo maturity"]) == 1
    assert g.repo_positions[0].status == "matured"


def test_reverse_repo_returns_unmatured_underlying_bill_at_contract_maturity():
    g = game()
    start = START
    bill_maturity = START + timedelta(days=120)
    contract_maturity = START + timedelta(days=60)
    security = SecuritySlice(
        security_id="CBB0099", face_value=250, tbill_rate=3.0,
        issue_date=start - timedelta(days=1), maturity_date=bill_maturity
    )
    g.repo_positions.append(RepoPosition(
        position_id="RRP0099", bank="B", action="Reverse Repo",
        start_date=start, maturity_date=contract_maturity, face_value=250,
        initial_cash=245, transaction_rate=4.0, securities=[security], status="active"
    ))
    flow, events = g.process_maturities(contract_maturity)
    assert flow < 0
    assert any(e["type"] == "Reverse Repo maturity" for e in events)
    assert g.market_inventory.total_face_value(contract_maturity) == 250
    assert g.repo_positions[0].status == "matured"
