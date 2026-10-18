import pytest
from datetime import date
from central_bank_engine_v13 import Decision, CentralBankGame


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
