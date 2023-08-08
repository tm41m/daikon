import requests
import os

DAIKON_HOST_URL = os.environ.get("DAIKON_HOST_URL")


def test_api_product_metrics_search_endpoint():
    url = DAIKON_HOST_URL + "/product-metrics/search"
    params = {"start_date": "2023-01-01", "end_date": "2023-01-02", "product_id": 1, "region_code": "ON"}
    response = requests.get(url, params=params)

    data = response.json()

    expected_data = [
        {
            "avg_price": "6.10",
            "avg_price_chng": "0.01",
            "calendar_date": "2023-01-02",
            "currency": "CAD",
            "md5_key": "1e4df936c94cc8f88cea811629cce539",
            "product_id": 1,
            "product_listings": 101,
            "product_listings_rtn": 98,
            "region_code": "ON",
            "unit": "/ 1kg",
        },
        {
            "avg_price": "6.09",
            "avg_price_chng": "0.01",
            "calendar_date": "2023-01-01",
            "currency": "CAD",
            "md5_key": "bd5f438be66323636bb227a81460d197",
            "product_id": 1,
            "product_listings": 100,
            "product_listings_rtn": 98,
            "region_code": "ON",
            "unit": "/ 1kg",
        },
    ]

    assert expected_data == data
