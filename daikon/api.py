from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_cors import cross_origin
from daikon.model import db, ma
from daikon.model.product_metrics import ProductMetrics, ProductMetricsSchema
from daikon.model.statcan_food_prices import StatcanFoodPrices, StatcanFoodPricesSchema
from daikon.model.statcan_cpi_monthly import StatcanCPIMonthly, StatcanCPIMonthlySchema
from daikon.auth import auth_required
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DAIKON_SQLALCHEMY_DATABASE_URI")
db.init_app(app)
ma.init_app(app)

cache = Cache(config={"DEBUG": True, "CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 604800})
cache.init_app(app)

whitelist_domains = ["https://*.static.observableusercontent.com"]


@app.route("/stores/<int:id>", methods=["GET"])
@auth_required
def get_stores(id):
    pass


@app.route("/product-listings/<int:id>", methods=["GET"])
@auth_required
def get_product_listings(id):
    pass


@app.route("/product-metrics/search", methods=["GET"])
@cache.cached(timeout=604800, query_string=True)
@cross_origin(whitelist_domains)
def get_product_metrics():
    query_params = request.args

    try:
        product_id = query_params["product_id"]
        start_date = query_params["start_date"]
    except KeyError:
        return (
            jsonify(
                {"error": "Invalid query params, refer to https://tm41m.io/docs/daikon/product_timeseries_metrics.html"}
            ),
            400,
        )

    region_code = query_params.get("region_code", None)
    census_division_name = query_params.get("census_division_name", None)
    end_date = query_params.get("end_date", datetime.now().strftime("%Y-%m-%d"))

    if (not census_division_name is None) and (region_code is None):
        return (
            jsonify(
                {
                    "error": "census_division_name cannot be passed without region_code, refer to https://tm41m.io/docs/daikon/product_timeseries_metrics.html"
                }
            ),
            400,
        )

    product_metrics = (
        ProductMetrics.query.filter(ProductMetrics.product_id == product_id)
        .filter(ProductMetrics.region_code == region_code)
        .filter(ProductMetrics.census_division_name == census_division_name)
        .filter(ProductMetrics.calendar_date.between(start_date, end_date))
    )

    res = product_metrics.all()
    schema = ProductMetricsSchema(many=True)
    output = schema.dump(res)

    return jsonify(output), 200


@app.route("/statcan-cpi-monthly/search", methods=["GET"])
@cache.cached(timeout=604800, query_string=True)
@cross_origin(whitelist_domains)
def get_statcan_cpi_monthly():
    query_params = request.args

    try:
        component_name = query_params["component_name"]
        start_date = query_params["start_date"]
    except KeyError:
        return (
            jsonify({"error": "Invalid query params, refer to https://tm41m.io/docs/daikon/statcan_cpi_monthly.html"}),
            400,
        )

    region_code = query_params.get("region_code", None)
    end_date = query_params.get("end_date", datetime.now().strftime("%Y-%m-%d"))

    statcan_cpi_monthly = (
        StatcanCPIMonthly.query.filter(StatcanCPIMonthly.component_name == component_name)
        .filter(StatcanCPIMonthly.region_code == region_code)
        .filter(StatcanCPIMonthly.calendar_date.between(start_date, end_date))
    )

    res = statcan_cpi_monthly.all()
    schema = StatcanCPIMonthlySchema(many=True)
    output = schema.dump(res)

    return jsonify(output), 200


@app.route("/statcan-food-prices/search", methods=["GET"])
@cache.cached(timeout=604800, query_string=True)
@cross_origin(whitelist_domains)
def get_statcan_food_prices():
    query_params = request.args

    try:
        product_name = query_params["product_name"]
        amount = query_params["amount"]
        unit = query_params["unit"]
        start_date = query_params["start_date"]
    except KeyError:
        return (
            jsonify(
                {"error": "Invalid query params, refer to https://tm41m.io/docs/daikon/product_timeseries_metrics.html"}
            ),
            400,
        )

    region_code = query_params.get("region_code", None)
    end_date = query_params.get("end_date", datetime.now().strftime("%Y-%m-%d"))

    statcan_food_prices = (
        StatcanFoodPrices.query.filter(StatcanFoodPrices.product_name == product_name)
        .filter(StatcanFoodPrices.amount == amount)
        .filter(StatcanFoodPrices.unit == unit)
        .filter(StatcanFoodPrices.region_code == region_code)
        .filter(StatcanFoodPrices.calendar_date.between(start_date, end_date))
    )

    res = statcan_food_prices.all()
    schema = StatcanFoodPricesSchema(many=True)
    output = schema.dump(res)

    return jsonify(output), 200


if __name__ == "__main__":
    app.run(debug=True)
