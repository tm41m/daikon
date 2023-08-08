BEGIN;

CREATE SCHEMA wolfram;

CREATE TABLE wolfram.product_timeseries_metrics (
    calendar_date DATE,
    region_code CHAR(2),
    product_id BIGINT,
    currency CHAR(3),
    unit VARCHAR(10),
    avg_price NUMERIC(32,2),
    avg_price_chng NUMERIC(32,6),
    product_listings BIGINT,
    product_listings_rtn BIGINT,
    md5_key CHAR(32)
);

INSERT INTO wolfram.product_timeseries_metrics VALUES
    ('2023-01-01', 'ON', 1, 'CAD', '/ 1kg', 6.09, 0.01, 100, 98, md5('2023-01-01' || '1' || 'ON')),
    ('2023-01-02', 'ON', 1, 'CAD', '/ 1kg', 6.10, 0.01, 101, 98, md5('2023-01-02' || '1' || 'ON')),
    ('2023-01-01', null, 1, 'CAD', '/ 1kg', 6.00, 0.01, 120, 98, md5('2023-01-01' || '1' || '')),
    ('2023-01-02', null, 1, 'CAD', '/ 1kg', 6.01, 0.01, 121, 98, md5('2023-01-02' || '1' || ''));

COMMIT;
