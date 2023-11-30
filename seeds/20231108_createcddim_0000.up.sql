BEGIN;

CREATE TABLE stahl.dim_census_division (
    id VARCHAR(4),
    name VARCHAR(100),
    type VARCHAR(3),
    land_area NUMERIC(32, 2),
    region_code CHAR(2)
);

INSERT INTO stahl.dim_census_division VALUES
    ('1201', 'Shelburne', 'CTY', 2462.5818, 'NS'),
    ('1206', 'Lunenburg', 'CTY', 2906.4723, 'NS'),
    ('2418', 'Montmagny', 'MRC', 1695.0914, 'QC'),
    ('3516', 'Kawartha Lakes', 'CDR', 3033.6565, 'ON');

COMMIT;
