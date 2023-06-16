from flask import Flask, jsonify, request
from daikon.model.dim import ProductListing, ProductListingSchema
from datetime import datetime

app = Flask(__name__)

now_iso = datetime.now()

product_listings = [
    ProductListing(1, 'White Onion', 1, 1, 1.69, 'lbs', 'CAD', 1, True, True, 1, now_iso, now_iso),
    ProductListing(2, 'White Onion', 1, 2, 2.69, 'lbs', 'CAD', 1, True, True, 1, now_iso, now_iso)
]

@app.route('/v1/dim/productlisting/id/<int:id>', methods=['GET'])
def get(id):

    product_listings_schema = ProductListingSchema(many=True)
    # product_listing_schema = ProductListingSchema()

    product_listing = product_listings_schema.dump(filter(lambda t: t.id == id, product_listings))

    return jsonify(product_listing)
