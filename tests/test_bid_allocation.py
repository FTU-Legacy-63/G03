import pytest
from datetime import date
from central_bank_engine_v13 import Decision, CentralBankGame

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
