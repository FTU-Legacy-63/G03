import pytest
from datetime import date
from central_bank_engine_v13 import Decision, CentralBankGame

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
