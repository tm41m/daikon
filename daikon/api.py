from flask import Flask, jsonify, request
from daikon.model.product_metrics import db, ma, ProductMetrics, ProductMetricsSchema
from daikon.auth import auth_required
from datetime import datetime
from flask_restful import Api, Resource

import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
db.init_app(app)
ma.init_app(app)
api = Api(app)

product_metric_schema = ProductMetricsSchema()


class ProductMetricsListResource(Resource):
    product_metric_schema = ProductMetricsSchema()

    product_metrics_schema = ProductMetricsSchema(many=True)

    def get(self):
        product_metrics = ProductMetrics.query.all()
        return self.product_metrics_schema(product_metrics)


api.add_resource(ProductMetricsListResource, "/product-metrics")


@app.route("/v1/stores/<int:id>", methods=["GET"])
@auth_required
def get_store(id):
    pass
    # product_listings_schema = ProductListingSchema(many=True)
    # product_listing_schema = ProductListingSchema()

    # product_listing = product_listings_schema.dump(filter(lambda t: t.id == id, product_listings))

    # return jsonify(product_listing)


@app.route("/v1/dim/productlisting/id/<int:id>", methods=["GET"])
@auth_required
def get_product_listing(id):
    pass
    # product_listings_schema = ProductListingSchema(many=True)
    # product_listing_schema = ProductListingSchema()

    # product_listing = product_listings_schema.dump(filter(lambda t: t.id == id, product_listings))

    # return jsonify(product_listing)


@app.route("/v1/product-metrics/search", methods=["GET"])
def get_product_metrics():
    product_metrics = ProductMetrics.query.all()
    res = product_metric_schema.dump(product_metrics)
    return jsonify(res)
    # region_code = request.args.get("region_code")
    # start_date = request.args.get("start_date")
    # end_date = request.args.get("end_date")
    # product_id = request.args.get("product_id")

    # eg = 6.0180962800875274 if region_code is None else 7.6900000000000000

    # chng = (
    #     (6.0180962800875274 - 6.0167400881057269) if region_code is None else (7.6900000000000000 - 7.6900000000000000)
    # )

    # product_metrics = {
    #     "calendar_date": start_date,
    #     "product_id": 1,
    #     "currency": "CAD",
    #     "unit": "/ 1kg",
    #     "avg_price": eg + 2,
    #     "avg_price_chng": chng,
    #     "product_listings": 1039,
    #     "product_listings_rtn": 876,
    # }

    return jsonify(product_metrics)


if __name__ == "__main__":
    app.run(debug=True)
