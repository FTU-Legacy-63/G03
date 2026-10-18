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
