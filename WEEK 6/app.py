from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from pathlib import Path
from central_bank_engine_v13 import CentralBankGame, Decision

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)
CORS(app)

# Game instance của phiên chơi hiện tại
game_instance = None

def _get_next_scenario_liquidity_demand():
    """Return the next phase demand after run_phase() advances the engine.

    The engine increments ``game_instance.phase`` before returning a PhaseResult,
    so get_scenario_liquidity_demand() now points at the upcoming phase.
    After Phase 3 there is no configured next phase, so expose JSON null instead
    of turning an otherwise successful phase into an API error.
    """
    try:
        return game_instance.get_scenario_liquidity_demand()
    except ValueError:
        return None

# FRONTEND
@app.route("/")
def index():
    return send_from_directory(str(BASE_DIR), "omo_refactored_v64.html")

# START GAME

@app.route("/api/start-game", methods=["POST"])
def start_game():
    global game_instance
    data = request.get_json(silent=True) or {}
    start_date_str = data.get(
        "start_date",
        "02/02/2025"
    )
    initial_rate = float(
        data.get(
            "initial_rate",
            3.95
        )
    )
    try:
        start_date = datetime.strptime(
            start_date_str,
            "%d/%m/%Y"
        ).date()

        # Tạo game mới
        game_instance = CentralBankGame(
            start_date=start_date,
            initial_interbank_rate=initial_rate,
            floor=0.5,
            cap=5.0
        )

        # Khởi tạo T-Bill ban đầu
        tb = game_instance.initialize_market_tbill(
            face_value=10000
        )

        # Scenario Demand
        scenario_liquidity_demand = (
            game_instance.get_scenario_liquidity_demand()
        )

        return jsonify({
            "status": "success",
            "current_date": game_instance.current_date.strftime("%d/%m/%Y"),
            "interbank_rate": game_instance.interbank_rate,
            "initial_interbank_rate": game_instance.interbank_rate,
            "scenario_liquidity_demand": scenario_liquidity_demand,
            "tbill_inventory": game_instance.tbill_inventory(),
            "repo_inventory": game_instance.repo_inventory(),
            "initial_tbill": {
                "id": tb.security_id,
                "rate": tb.rate,
                "maturity_date":
                    tb.maturity_date.strftime("%d/%m/%Y")
            }
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


# =========================================================
# RUN PHASE
# =========================================================

@app.route("/api/run-phase", methods=["POST"])
def run_phase():
    global game_instance
    if game_instance is None:
        return jsonify({
            "status": "error",
            "message": "Game has not been started yet."
        }), 400

    data = request.get_json(silent=True) or {}

    try:
        # Nhận Decision từ frontend
        auction_method = data.get("auction_method")
        omo_action = data.get("omo_action")
        volume = float(data.get("volume",0)
        )
        pricing_method = data.get("pricing_method")
        repo_rate = data.get("repo_rate")

        if repo_rate is not None:
            repo_rate = float(repo_rate)

        # Expected Inflation
        expected_inflation = data.get(
            "expected_inflation"
        )

        if expected_inflation is not None:
            expected_inflation = float(
                expected_inflation
            )


        # -------------------------------------------------
        # Tạo Decision
        # -------------------------------------------------

        decision = Decision(
            auction_method=auction_method,
            omo_action=omo_action,
            volume=volume,
            pricing_method=pricing_method,
            repo_rate=repo_rate,
            expected_inflation=expected_inflation
        )


        # -------------------------------------------------
        # Engine gọi:
        # get_scenario_liquidity_demand()
        # -------------------------------------------------

        result = game_instance.run_phase(
            None,
            decision
        )

        # -------------------------------------------------
        # Auction bids
        # -------------------------------------------------

        bids = []

        for b in result.auction_bids:

            bids.append({

                "rank":
                    b.rank,

                "bank":
                    b.bank,

                "bid_rate":
                    b.bid_rate,

                "settlement_rate":
                    b.settlement_rate,

                "bid_volume":
                    b.bid_volume,

                "real_volume":
                    b.real_volume,

                "price":
                    b.price,

                "won":
                    b.won,

                "status":
                    "Trúng thầu"
                    if b.won
                    else
                    "Không trúng thầu"

            })


        # -------------------------------------------------
        # DEBUG REPO INVENTORY
        # -------------------------------------------------

        repo_debug = game_instance.repo_inventory()

        print("========== DEBUG REPO INVENTORY ==========")
        print("Number of repo positions:", len(repo_debug))
        print("Repo inventory:", repo_debug)
        print("==========================================")


        # -------------------------------------------------
        # JSON trả về frontend
        # -------------------------------------------------

        response = {
            "status": "success",
            "phase": result.phase,
            "phase_date": result.phase_date.strftime("%d/%m/%Y"),


            # LIQUIDITY
            "scenario_liquidity_demand": result.scenario_liquidity_demand,
            "next_scenario_liquidity_demand":
                _get_next_scenario_liquidity_demand(),
            "unmet_from_previous_phase": result.unmet_from_previous_phase,
            "real_liquidity_demand": result.real_liquidity_demand,
            "supply": result.supply,
            "maturity_volume": result.maturity_volume,
            "total_supply": result.total_supply,
            "liquidity_gap": result.liquidity_gap,
            "liquidity_pressure": result.liquidity_pressure,

            # INTERBANK
            "previous_interbank_rate": result.previous_interbank_rate,

            "interbank_rate":
                result.interbank_rate,


            # AUCTION
            "total_cash_bid_volume":
                result.total_cash_bid_volume,

            "total_bid_volume":
                result.total_bid_volume,

            "total_real_volume":
                result.total_real_volume,

            "win_rate":
                result.win_rate,

            "bids":
                bids,


            # INVENTORY
            "tbill_inventory":
                game_instance.tbill_inventory(),

            "repo_inventory":
                game_instance.repo_inventory(),

            "maturity_events":
                result.maturity_events,


            # MACRO
            "expected_inflation":
                result.expected_inflation,

            "real_interest_rate":
                result.real_interest_rate,

            "output_gap":
                result.output_gap,

            "gdp_growth":
                result.gdp_growth,

            "inflation":
                result.inflation
        }


        return jsonify(response)


    except Exception as e:

        return jsonify({

            "status":
                "error",

            "message":
                str(e)

        }), 400


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":

    print(
        "Central Bank OMO Server running at:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
