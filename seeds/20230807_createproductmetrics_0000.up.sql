BEGIN;

CREATE SCHEMA wolfram;

CREATE TABLE wolfram.product_timeseries_metrics (
    calendar_date DATE,
    region_code CHAR(2),
    product_id BIGINT,
    currency CHAR(3),
    unit VARCHAR(10),
    avg_price NUMERIC(32,2),
    avg_price_chng NUMBER(32,2),
    product_listings BIGINT,
    product_listings_rtn BIGINT,
    md5_key CHAR(32)
;

COMMIT
;