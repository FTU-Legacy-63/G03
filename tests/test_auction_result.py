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
