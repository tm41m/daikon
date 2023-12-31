BEGIN;

CREATE SCHEMA wolfram;

CREATE TABLE wolfram.product_timeseries_metrics (
    calendar_date DATE,
    region_code CHAR(2),
    census_division_name TEXT,
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
    ('2023-01-01', 'ON', 'Wellington', 1, 'CAD', '/ 1kg', 6.45, 0.01, 110, 98, md5('2023-01-01' || '1' || 'ON' || 'Wellington')),
    ('2023-01-02', 'ON', 'Wellington', 1, 'CAD', '/ 1kg', 6.46, 0.01, 111, 98, md5('2023-01-02' || '1' || 'ON' || 'Wellington')),
    ('2023-01-01', 'QC', 'La Matapédia', 1, 'CAD', '/ 1kg', 6.47, 0.01, 110, 98, md5('2023-01-01' || '1' || 'QC' || 'La Matapédia')),
    ('2023-01-02', 'QC', 'La Matapédia', 1, 'CAD', '/ 1kg', 6.48, 0.01, 111, 98, md5('2023-01-02' || '1' || 'QC' || 'La Matapédia')),
    ('2023-01-01', 'ON', null, 1, 'CAD', '/ 1kg', 6.09, 0.01, 100, 98, md5('2023-01-01' || '1' || 'ON' || '')),
    ('2023-01-02', 'ON', null, 1, 'CAD', '/ 1kg', 6.10, 0.01, 101, 98, md5('2023-01-02' || '1' || 'ON' || '')),
    ('2023-01-01', null, null, 1, 'CAD', '/ 1kg', 6.00, 0.01, 120, 98, md5('2023-01-01' || '1' || '' || '')),
    ('2023-01-02', null, null, 1, 'CAD', '/ 1kg', 6.01, 0.01, 121, 98, md5('2023-01-02' || '1' || '' || ''));

COMMIT;
