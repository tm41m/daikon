from flask import Flask, jsonify, request

app = Flask(__name__)

prices = [
    {
        "product_name": "white onion",
        "prices":[
            {
                "store_id": 0,
                "price": 1.0
            },
            {
                "store_id": 1,
                "price": 1.2
            }
        ]
    }
    , {
        "product_name": "celery",
        "prices": [
            {
                "store_id": 0,
                "price": 1.2
            }
        ]
    }
]

@app.route('/prices')
def get_prices():
    return jsonify(prices)

# @app.route('/prices', methods=['POST'])
# def add_prices():
#     prices.append(request.get_json())

#     return '', 204
