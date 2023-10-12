BEGIN;

CREATE TABLE stahl.statcan_cpi_monthly (
    calendar_date DATE,
    time_grain TEXT,
    region_code CHAR(2),
    component_name TEXT,
    cpi NUMERIC(32,2),
    previous_cpi NUMERIC(32,2),
    cpi_chng NUMERIC(32,4),
    r_dguid TEXT,
    r_uom TEXT,
    md5_key CHAR(32) PRIMARY KEY
);

INSERT INTO stahl.statcan_cpi_monthly VALUES
    ('2023-01-01', 'monthly', 'ON', 'Food', 100.20, 99.20, 1.0000, '1', '2002=100', md5('10000'));

COMMIT;
