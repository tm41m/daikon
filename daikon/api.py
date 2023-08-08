from flask import Flask, jsonify, request
from flask_caching import Cache
from daikon.model.product_metrics import db, ma, ProductMetrics, ProductMetricsSchema
from daikon.auth import auth_required
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DAIKON_SQLALCHEMY_DATABASE_URI")
db.init_app(app)
ma.init_app(app)

cache = Cache(config={"DEBUG": True, "CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 604800})
cache.init_app(app)


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
    end_date = query_params.get("end_date", datetime.now().strftime("%Y-%m-%d"))

    product_metrics = (
        ProductMetrics.query.filter(ProductMetrics.product_id == product_id)
        .filter(ProductMetrics.region_code == region_code)
        .filter(ProductMetrics.calendar_date.between(start_date, end_date))
    )

    res = product_metrics.all()
    schema = ProductMetricsSchema(many=True)
    output = schema.dump(res)

    return jsonify(output), 200


if __name__ == "__main__":
    app.run(debug=True)
