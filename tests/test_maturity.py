import pytest
from datetime import date
from central_bank_engine_v13 import Decision, CentralBankGame

START = date(2025, 1, 1)

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
