import requests
import os
import psycopg2

DAIKON_HOST_URL = os.environ.get("DAIKON_HOST_URL")
PG_HOST = os.environ.get("DAIKON_PG_HOST")
PG_PORT = os.environ.get("DAIKON_PG_PORT")
PG_DBNAME = os.environ.get("DAIKON_PG_DBNAME")
PG_USERNAME = os.environ.get("DAIKON_PG_USERNAME")
PG_PASSWORD = os.environ.get("DAIKON_PG_PASSWORD")


def test_api_caching():
    url = DAIKON_HOST_URL + "/product-metrics/search"
    params = {"start_date": "2023-01-01", "end_date": "2023-01-01", "product_id": 1, "region_code": "ON"}
    response = requests.get(url, params=params)

    data = response.json()

    assert data[0]["avg_price"] == "6.09"

    def temp_set_price(price_val, **params):
        ddl = """
            update wolfram.product_timeseries_metrics
            set avg_price = {price_val}
            where calendar_date between '{start_date}' and '{end_date}'
              and product_id = {product_id} and region_code='{region_code}'
        """.format(
            price_val=price_val,
            start_date=params["start_date"],
            end_date=params["end_date"],
            product_id=params["product_id"],
            region_code=params["region_code"],
        )

        conn = psycopg2.connect(host=PG_HOST, database=PG_DBNAME, user=PG_USERNAME, password=PG_PASSWORD, port=PG_PORT)
        cur = conn.cursor()
        cur.execute(ddl)

    assert data[0]["avg_price"] == "6.09"

    temp_set_price(6.10, **params)

    response2 = requests.get(url, params=params)

    data2 = response2.json()

    assert data2[0]["avg_price"] == "6.09"

    temp_set_price(6.09, **params)
