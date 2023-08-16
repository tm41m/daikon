BEGIN;

CREATE SCHEMA stahl;

CREATE TABLE stahl.statcan_food_prices (
    calendar_date DATE,
    time_grain TEXT,
    region_code CHAR(2),
    r_product_name TEXT,
    product_name TEXT,
    amount NUMERIC(32,2),
    unit VARCHAR(10),
    currency CHAR(3),
    price NUMERIC(32,2),
    previous_price NUMERIC(32,2),
    price_chng NUMERIC(32,4),
    r_dguid TEXT,
    md5_key CHAR(32)
);

INSERT INTO stahl.statcan_food_prices VALUES
    ('2023-01-01', 'monthly', 'ON', 'Onions', 'Onions', 1, 'kg', 'CAD', 5.30, 5.23, 0.0001, '0001', md5('0001'));

COMMIT;
