import pytest
from datetime import date
from central_bank_engine_v13 import Decision, CentralBankGame

def test_macro_results_are_published_every_three_phases():
    game = CentralBankGame(
        start_date=date(2025, 2, 2),
        initial_interbank_rate=3.95,
        seed=42,
    )
    # Phase 1: nhập Expected Inflation
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

    # Phase 2: chưa công bố kết quả
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

    # Phase 3: công bố kết quả
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
