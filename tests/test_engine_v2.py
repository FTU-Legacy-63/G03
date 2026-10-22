"""Expanded regression tests for central_bank_engine_v13.py.

Run from the folder containing both files:
    python -m pytest -v test_engine_v2.py

Coverage report (requires coverage.py):
    python -m coverage run -m pytest -q test_engine_v2.py
    python -m coverage report -m central_bank_engine_v13.py

Scope note: frontend-managed input validation is not expanded here. The
existing macro formula expectations are retained as regression checks; this
suite focuses on auction mechanics, inventory, maturities, and phase flow.
"""

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

# ---------------------------------------------------------------------------
# Expanded regression coverage (v2)
# Assumption: frontend controls user inputs; macro formulas are accepted as
# the model's agreed specification. These tests focus on backend operations.
# ---------------------------------------------------------------------------

from central_bank_engine_v13 import (
    AuctionBid,
    MarketTBillInventory,
    excel_round,
    whole,
    whole_distribution,
    price,
    repayment,
)


@pytest.mark.parametrize(
    ("value", "digits", "expected"),
    [
        (1.5, 0, 2.0),
        (-1.5, 0, -2.0),
        (2.345, 2, 2.35),
        (-2.345, 2, -2.35),
        (4.0, 2, 4.0),
    ],
)
def test_excel_round_matches_half_away_from_zero(value, digits, expected):
    assert excel_round(value, digits) == expected


@pytest.mark.parametrize(
    ("weights", "total"),
    [
        ([1, 1, 1], 10),
        ([0.2, 0.4, 0.4], 101),
        ([0, 1, 0], 9),
        ([1, 2, 3, 4, 5], 1000),
        ([1, 2, 3], 0),
    ],
)
def test_whole_distribution_sums_to_target_and_never_goes_negative(weights, total):
    allocation = whole_distribution(weights, total)
    assert len(allocation) == len(weights)
    assert all(isinstance(x, float) and x >= 0 for x in allocation)
    assert sum(allocation) == max(0, whole(total))


def test_auction_table_serializes_all_bid_fields_including_cash_volume():
    bid = AuctionBid(
        rank=1,
        bank="A",
        bid_rate=4.0,
        settlement_rate=4.0,
        bid_volume=1000,
        real_volume=500,
        price=498.0,
        won=True,
        cash_bid_volume=450.0,
    )
    # PhaseResult owns auction_table; build it with the minimum required fields.
    from central_bank_engine_v13 import PhaseResult
    result = PhaseResult(
        phase=1, phase_date=START, decision=decision(),
        scenario_liquidity_demand=1, unmet_from_previous_phase=0,
        real_liquidity_demand=1, supply=1, maturity_volume=0,
        total_supply=1, liquidity_gap=0, previous_interbank_rate=4,
        interbank_rate=4, total_cash_bid_volume=450, total_bid_volume=1000,
        total_real_volume=500, win_rate=4, auction_bids=[bid], maturity_events=[]
    )
    row = result.auction_table()[0]
    assert row["bank"] == "A"
    assert row["cash_bid_volume"] == 450.0
    assert row["real_volume"] == 500.0


def test_inventory_eligible_volume_respects_remaining_maturity():
    inv = MarketTBillInventory()
    inv.add_lot(100, START, 3.0, tenor_days=30)
    inv.add_lot(200, START, 4.0, tenor_days=90)
    inv.add_lot(300, START, 5.0, tenor_days=120)
    assert inv.eligible_face_value(START, min_remaining_days=60) == 500
    assert inv.eligible_face_value(START, min_remaining_days=90) == 500
    assert inv.eligible_face_value(START + timedelta(days=31), 60) == 300


def test_take_fifo_skips_ineligible_lot_and_uses_eligible_fifo_order():
    inv = MarketTBillInventory()
    short = inv.add_lot(100, START, 2.0, tenor_days=30)
    older_eligible = inv.add_lot(200, START + timedelta(days=1), 3.0, tenor_days=120)
    newer_eligible = inv.add_lot(300, START + timedelta(days=2), 4.0, tenor_days=120)
    slices = inv.take_fifo(250, START, min_remaining_days=60)
    assert [(x.security_id, x.face_value) for x in slices] == [
        (older_eligible.security_id, 200), (newer_eligible.security_id, 50)
    ]
    remaining = {x.security_id: x.face_value for x in inv.lots}
    assert remaining[short.security_id] == 100
    assert remaining[newer_eligible.security_id] == 250


def test_return_slices_restores_existing_lot_and_does_not_recreate_matured_slice():
    inv = MarketTBillInventory()
    lot = inv.add_lot(100, START, 3.0, tenor_days=120)
    slices = [
        SecuritySlice(lot.security_id, 25, lot.rate, lot.issue_date, lot.maturity_date),
        SecuritySlice("MATURED-1", 40, 2.0, START - timedelta(days=120), START),
        SecuritySlice("MISSING-1", 30, 4.0, START, START + timedelta(days=120)),
    ]
    inv.return_slices(slices, START)
    volumes = {x.security_id: x.face_value for x in inv.lots}
    assert volumes[lot.security_id] == 125
    assert "MATURED-1" not in volumes
    assert volumes["MISSING-1"] == 30


@pytest.mark.parametrize(
    ("action", "rate", "rld", "expected_min", "expected_max"),
    [
        ("Buy Securities", 0.49, 1000, 100, 300),    # injection, matches need
        ("Buy Securities", 0.49, -1000, 30, 150),   # injection, against need
        ("Buy Securities", 4.00, 1000, 900, 1000),
        ("Buy Securities", 5.01, 1000, 800, 900),
        ("Sell Securities", 0.49, -1000, 100, 300), # absorption, matches need
        ("Sell Securities", 0.49, 1000, 30, 150),   # absorption, against need
        ("Sell Securities", 4.00, -1000, 800, 900),
        ("Sell Securities", 5.01, -1000, 900, 1000),
        ("Repo", 4.00, -1000, 800, 900),
        ("Reverse Repo", 4.00, 1000, 900, 1000),
    ],
)
def test_volume_auction_rate_bands(action, rate, rld, expected_min, expected_max):
    g = game()
    amount = g._volume_total_cash_bid_for_action(action, rld, 1000, rate)
    assert expected_min <= amount <= expected_max


@pytest.mark.parametrize("action", ["Buy Securities", "Sell Securities", "Repo", "Reverse Repo"])
def test_cash_bid_conversion_works_for_each_omo_instrument(action):
    g = game(tbill_tenor_days=90, repo_tenor_days=60)
    actual = g._cash_bid_to_face_volume(1000, action, 4.0)
    days = 60 if action == "Reverse Repo" else 90
    expected = whole(1000 * (1 + 4.0 * days / 36500))
    assert actual == expected


@pytest.mark.parametrize(
    ("action", "expected_max"),
    [
        ("Buy Securities", 7000),
        ("Reverse Repo", 5000),
        ("Sell Securities", 10000),
        ("Repo", 10000),
    ],
)
def test_max_real_respects_instrument_inventory_constraints(action, expected_max):
    g = game(repo_tenor_days=60)
    g.market_inventory.add_lot(2000, START, 3.0, tenor_days=30)
    g.market_inventory.add_lot(3000, START, 4.0, tenor_days=90)
    g.market_inventory.add_lot(2000, START, 4.0, tenor_days=120)
    assert g._max_real(action, 10000) == expected_max


@pytest.mark.parametrize("method", ["Interest-rate auction", "Volume auction"])
@pytest.mark.parametrize("action", ["Buy Securities", "Sell Securities", "Repo", "Reverse Repo"])
def test_auction_all_action_and_method_combinations_have_consistent_results(method, action):
    g = game(tbill_tenor_days=120, repo_tenor_days=60)
    g.market_inventory.add_lot(30000, START, 4.0, tenor_days=120)
    if method == "Interest-rate auction":
        d = Decision(
            auction_method=method, omo_action=action, volume=10000,
            pricing_method="Multi-price"
        )
    else:
        d = Decision(
            auction_method=method, omo_action=action, volume=10000,
            repo_rate=4.0
        )
    result = g.run_auction(d, rld=4000)
    bids = result["bids"]
    assert len(bids) == 5
    assert result["total_real_volume"] == sum(b.real_volume for b in bids)
    assert result["total_real_volume"] <= d.volume
    assert all(b.real_volume >= 0 and b.bid_volume >= 0 for b in bids)
    assert all(b.won == (b.real_volume > 0) for b in bids)
    if action in ("Buy Securities", "Reverse Repo"):
        assert result["supply"] >= 0
    else:
        assert result["supply"] <= 0
    if action in ("Repo", "Reverse Repo") and result["total_real_volume"] > 0:
        assert g.repo_positions
        assert all(p.action == action for p in g.repo_positions)


def test_reverse_repo_only_consumes_securities_with_sufficient_remaining_maturity():
    g = game(repo_tenor_days=60)
    short = g.market_inventory.add_lot(100, START, 3.0, tenor_days=30)
    eligible = g.market_inventory.add_lot(5000, START, 4.0, tenor_days=120)
    d = Decision(
        auction_method="Interest-rate auction", omo_action="Reverse Repo",
        volume=2000, pricing_method="Single-price"
    )
    result = g.run_auction(d, rld=4000)
    remaining = {x.security_id: x.face_value for x in g.market_inventory.lots}
    assert remaining[short.security_id] == 100
    assert result["total_real_volume"] <= 5000
    assert remaining.get(eligible.security_id, 0) >= 0


def test_forecast_maturities_is_read_only_and_includes_bill_and_repo_flows():
    g = game()
    g.market_inventory.add_lot(500, START, 3.0, tenor_days=30)
    g.repo_positions.append(RepoPosition(
        position_id="RP-FORECAST", bank="A", action="Repo",
        start_date=START, maturity_date=START + timedelta(days=60),
        face_value=100, initial_cash=100, transaction_rate=10.0,
        securities=[], status="active"
    ))
    cutoff = START + timedelta(days=60)
    before_inventory = g.market_inventory.snapshot()
    before_status = g.repo_positions[0].status
    forecast = g._forecast_maturities(cutoff)
    expected_repo = repayment(100, 10.0, 60)
    assert forecast == excel_round(500 + expected_repo, 2)
    assert g.market_inventory.snapshot() == before_inventory
    assert g.repo_positions[0].status == before_status


@pytest.mark.parametrize(
    ("action", "expected_sign"),
    [("Repo", 1), ("Reverse Repo", -1)],
)
def test_maturity_forecast_has_correct_repo_contract_sign(action, expected_sign):
    g = game()
    g.repo_positions.append(RepoPosition(
        position_id="RP-SIGN", bank="A", action=action,
        start_date=START, maturity_date=START + timedelta(days=60),
        face_value=100, initial_cash=100, transaction_rate=5.0,
        securities=[], status="active"
    ))
    forecast = g._forecast_maturities(START + timedelta(days=60))
    assert forecast * expected_sign > 0
    assert g.repo_positions[0].status == "active"


def test_same_bill_maturity_across_inventory_and_reverse_repo_is_merged():
    g = game()
    bill = g.market_inventory.add_lot(50, START, 3.0, tenor_days=30)
    security = SecuritySlice(
        security_id=bill.security_id, face_value=100, tbill_rate=3.0,
        issue_date=START - timedelta(days=60), maturity_date=START + timedelta(days=30)
    )
    g.repo_positions.append(RepoPosition(
        position_id="RRP-MERGE", bank="A", action="Reverse Repo",
        start_date=START, maturity_date=START + timedelta(days=60),
        face_value=100, initial_cash=100, transaction_rate=4.0,
        securities=[security], status="active"
    ))
    total, events = g.process_maturities(START + timedelta(days=30))
    bill_events = [e for e in events if e["type"] == "SBV Bill maturity"]
    assert total == 150
    assert len(bill_events) == 1
    assert bill_events[0]["volume"] == 150
    assert bill_events[0]["cash_flow"] == 150
    assert g.repo_positions[0].status == "active"


def test_repo_inventory_only_lists_active_positions_with_future_maturity():
    g = game()
    g.repo_positions.extend([
        RepoPosition("RP-A", "A", "Repo", START, START + timedelta(days=60),
                     100, 100, 4.0, [], "active"),
        RepoPosition("RP-B", "B", "Repo", START, START, 100, 100, 4.0, [], "active"),
        RepoPosition("RP-C", "C", "Repo", START, START + timedelta(days=60),
                     100, 100, 4.0, [], "matured"),
    ])
    rows = g.repo_inventory()
    assert [row["repo_id"] for row in rows] == ["RP-A"]


def test_nine_phase_sequence_completes_and_publishes_macro_at_checkpoints():
    g = game()
    results = []
    for phase in range(1, 10):
        expected = 4.0 if phase in (1, 4, 7) else None
        d = decision(enabled=False, expected=expected)
        result = g.run_phase(-999999, d)
        results.append(result)
        assert result.phase == phase
        assert result.auction_bids == []
        assert result.supply == 0
        expected_demands = {1: 4000.0, 2: 6000.0, 3: 3000.0, 4: -4000.0, 5: -2500.0, 6: -4000.0, 7: 500.0, 8: 1500.0, 9: -3000.0}
        assert result.scenario_liquidity_demand == expected_demands[phase]
    assert g.phase == 10
    assert len(g.history) == 9
    assert [r.phase for r in results if r.gdp_growth is not None] == [3, 6, 9]
    assert [r.phase for r in results if r.inflation is not None] == [3, 6, 9]
    assert results[-1].phase_date == START + timedelta(days=270)


@pytest.mark.parametrize(
    ("phase", "expected"),
    [
        (1, 4000.0), (2, 6000.0), (3, 3000.0),
        (4, -4000.0), (5, -2500.0), (6, -4000.0),
        (7, 500.0), (8, 1500.0), (9, -3000.0),
    ],
)
def test_scenario_liquidity_demand_is_configured_for_every_phase(phase, expected):
    g = game()
    g.phase = phase
    assert g.get_scenario_liquidity_demand() == expected


def test_disabled_auction_does_not_create_repo_positions():
    g = game()
    result = g.run_phase(0, decision(action="Repo", volume=10000, enabled=False, expected=4.0))
    assert result.auction_bids == []
    assert result.total_real_volume == 0
    assert result.supply == 0
    assert g.repo_positions == []


def test_auction_with_zero_volume_returns_zero_real_volume():
    g = game()
    g.initialize_market_tbill(face_value=10000, rate=4.0)
    d = Decision(
        auction_method="Interest-rate auction", omo_action="Buy Securities",
        volume=0, pricing_method="Single-price"
    )
    out = g.run_auction(d, rld=4000)
    assert out["total_real_volume"] == 0
    assert sum(b.real_volume for b in out["bids"]) == 0
    assert not any(b.won for b in out["bids"])


def test_security_price_and_repo_repayment_helpers_are_consistent():
    assert price(1000, 5.0, 90) == pytest.approx(1000 / (1 + 5.0 * 90 / 36500))
    assert repayment(1000, 5.0, 90) == pytest.approx(1000 * (1 + 5.0 * 90 / 36500))
    assert price(1000, 5.0, -5) == 1000


def test_initial_tbill_rate_is_reproducible_with_same_seed():
    g1 = game()
    g2 = game()
    assert g1.initial_tbill_rate() == g2.initial_tbill_rate()


def test_phase_updates_date_rate_history_and_phase_counter_consistently():
    g = game(phase_days=28)
    old_date = g.current_date
    old_rate = g.interbank_rate
    result = g.run_phase(4000, decision(enabled=False, expected=4.0))
    assert result.previous_interbank_rate == old_rate
    assert result.phase_date == old_date + timedelta(days=28)
    assert g.current_date == result.phase_date
    assert g.interbank_rate == result.interbank_rate
    assert g.phase == 2
    assert g.history[-1] is result


def test_zero_or_nonpositive_inventory_lot_is_not_added():
    inv = MarketTBillInventory()
    assert inv.add_lot(0, START, 3.0) is None
    assert inv.add_lot(-10, START, 3.0) is None
    assert inv.lots == []


def test_cash_bid_conversion_returns_zero_for_zero_cash_bid():
    g = game()
    for action in ("Buy Securities", "Sell Securities", "Repo", "Reverse Repo"):
        assert g._cash_bid_to_face_volume(0, action, 4.0) == 0


def test_cash_bid_conversion_stops_after_consuming_exact_reference_lot_value():
    g = game()
    first = g.market_inventory.add_lot(100, START, 4.0, tenor_days=90)
    g.market_inventory.add_lot(1000, START + timedelta(days=1), 5.0, tenor_days=120)
    cash_value_first_lot = first.face_value / (1 + first.rate * 90 / 36500)
    converted = g._cash_bid_to_face_volume(cash_value_first_lot, "Buy Securities", 4.0)
    assert converted == 100


def test_volume_auction_zero_volume_produces_no_awards():
    g = game()
    d = Decision(
        auction_method="Volume auction", omo_action="Sell Securities",
        volume=0, repo_rate=4.0
    )
    out = g.run_auction(d, rld=4000)
    assert out["total_cash_bid_volume"] == 0
    assert out["total_bid_volume"] == 0
    assert out["total_real_volume"] == 0
    assert all(b.real_volume == 0 and not b.won for b in out["bids"])


def test_volume_auction_prorates_awards_when_bid_demand_exceeds_offer():
    g = game(tbill_tenor_days=120)
    g.market_inventory.add_lot(20000, START, 4.0, tenor_days=120)
    d = Decision(
        auction_method="Volume auction", omo_action="Buy Securities",
        volume=1000, repo_rate=4.0
    )
    out = g.run_auction(d, rld=4000)
    assert out["total_bid_volume"] > out["total_real_volume"]
    assert out["total_real_volume"] == 1000
    assert sum(b.real_volume for b in out["bids"]) == 1000
    assert all(b.real_volume >= 0 for b in out["bids"])


def test_forecast_includes_reverse_repo_underlying_bill_maturity_before_contract():
    g = game()
    sec = SecuritySlice(
        security_id="UNDERLYING-1", face_value=250, tbill_rate=3.0,
        issue_date=START - timedelta(days=60), maturity_date=START + timedelta(days=30)
    )
    g.repo_positions.append(RepoPosition(
        position_id="RRP-FORECAST", bank="A", action="Reverse Repo",
        start_date=START, maturity_date=START + timedelta(days=60),
        face_value=250, initial_cash=245, transaction_rate=4.0,
        securities=[sec], status="active"
    ))
    forecast = g._forecast_maturities(START + timedelta(days=30))
    assert forecast == 250
    assert sec.face_value == 250  # Forecasting must not mark the slice as matured.
    assert g.repo_positions[0].status == "active"


def test_process_maturities_defaults_to_current_date():
    g = game()
    g.market_inventory.add_lot(150, START - timedelta(days=90), 3.0, tenor_days=90)
    total, events = g.process_maturities()
    assert total == 150
    assert len(events) == 1
    assert events[0]["type"] == "SBV Bill maturity"


def test_tbill_inventory_snapshot_excludes_matured_lots():
    g = game()
    g.market_inventory.add_lot(100, START, 3.0, tenor_days=30)
    g.market_inventory.add_lot(200, START, 4.0, tenor_days=90)
    snapshot = g.tbill_inventory()
    assert len(snapshot) == 2
    assert g.remaining_unmatured_tbill_volume() == 300
    g.current_date = START + timedelta(days=31)
    snapshot = g.tbill_inventory()
    assert len(snapshot) == 1
    assert snapshot[0]["remaining_volume"] == 200
    assert g.remaining_unmatured_tbill_volume() == 200


def test_game_rejects_phase_beyond_configured_scenario():
    g = game()
    g.phase = 10
    with pytest.raises(ValueError, match="not configured for Phase 10"):
        g.get_scenario_liquidity_demand()
