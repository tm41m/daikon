BEGIN;

CREATE TABLE stahl.dim_census_division (
    id CHAR(4),
    dguid CHAR(21),
    census_division_name CHAR(50),
    census_division_type CHAR(6),
    land_area NUMERIC(32, 2),
    region_code CHAR(2),
    md5_key CHAR(32)
);

INSERT INTO stahl.dim_census_division VALUES
    ('1201', '2021A00031201', 'Shelburne', 'CTY', 2462.5818, 'NS', md5('1201' || '15' || 'Shelburne' )),
    ('1206', '20', '2021A00031206', 'Lunenburg', 'CTY', 2906.4723, 'NS', md5('1206' || '20' || 'Lunenburg')),
    ('2418', '65', '2021A00032418', 'Montmagny', 'MRC', 1695.0914, 'QC', md5('2418' || '65' || 'Montmagny')),
    ('3516', '157', '2021A00033516', 'Kawartha Lakes', 'CDR', 3033.6565, 'ON', md5('3516' || '157' || 'Kawartha Lakes'));

COMMIT;
