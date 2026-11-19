
-- Remove previously generated tables.

DROP TABLE IF EXISTS rejected_inventory_movements;
DROP TABLE IF EXISTS clean_inventory_movements;
DROP TABLE IF EXISTS inventory_summary;


-- 1. Identify rejected records and their problems.

CREATE TABLE rejected_inventory_movements AS

SELECT
    *,

    RTRIM(
        CASE
            WHEN TRIM(COALESCE(movement_id, '')) = ''
            THEN 'Missing movement ID; '
            ELSE ''
        END ||

        CASE
            WHEN TRIM(COALESCE(movement_id, '')) IN (
                SELECT TRIM(movement_id)
                FROM raw_inventory_movements
                WHERE TRIM(COALESCE(movement_id, '')) != ''
                GROUP BY TRIM(movement_id)
                HAVING COUNT(*) > 1
            )
            THEN 'Duplicate movement ID; '
            ELSE ''
        END ||

        CASE
            WHEN TRIM(COALESCE(product_id, '')) = ''
            THEN 'Missing product ID; '
            ELSE ''
        END ||

        CASE
            WHEN date(movement_date) IS NULL
              OR LENGTH(movement_date) != 10
            THEN 'Invalid movement date; '
            ELSE ''
        END ||

        CASE
            WHEN UPPER(TRIM(movement_type)) NOT IN ('IN', 'OUT')
            THEN 'Invalid movement type; '
            ELSE ''
        END ||

        CASE
            WHEN CAST(quantity AS INTEGER) <= 0
            THEN 'Invalid quantity; '
            ELSE ''
        END ||

        CASE
            WHEN CAST(unit_cost AS REAL) <= 0
            THEN 'Invalid unit cost; '
            ELSE ''
        END,

        '; '

    ) AS rejection_reason

FROM raw_inventory_movements

WHERE

    TRIM(COALESCE(movement_id, '')) = ''

    OR TRIM(COALESCE(movement_id, '')) IN (
        SELECT TRIM(movement_id)
        FROM raw_inventory_movements
        WHERE TRIM(COALESCE(movement_id, '')) != ''
        GROUP BY TRIM(movement_id)
        HAVING COUNT(*) > 1
    )

    OR TRIM(COALESCE(product_id, '')) = ''

    OR date(movement_date) IS NULL
    OR LENGTH(movement_date) != 10

    OR UPPER(TRIM(movement_type)) NOT IN ('IN', 'OUT')

    OR CAST(quantity AS INTEGER) <= 0

    OR CAST(unit_cost AS REAL) <= 0;


-- 2. Keep only valid records and standardize their values.

CREATE TABLE clean_inventory_movements AS

SELECT
    movement_id,
    movement_date,
    TRIM(product_id) AS product_id,
    TRIM(product_name) AS product_name,
    UPPER(TRIM(category)) AS category,
    TRIM(supplier_id) AS supplier_id,
    TRIM(warehouse_id) AS warehouse_id,
    UPPER(TRIM(movement_type)) AS movement_type,
    CAST(quantity AS INTEGER) AS quantity,
    CAST(unit_cost AS REAL) AS unit_cost,
    TRIM(reference_number) AS reference_number,

    CAST(quantity AS INTEGER) *
    CAST(unit_cost AS REAL) AS movement_value,

    CASE
        WHEN UPPER(TRIM(movement_type)) = 'IN'
        THEN CAST(quantity AS INTEGER)

        WHEN UPPER(TRIM(movement_type)) = 'OUT'
        THEN -CAST(quantity AS INTEGER)
    END AS signed_quantity

FROM raw_inventory_movements

WHERE

    TRIM(COALESCE(movement_id, '')) != ''

    AND TRIM(movement_id) NOT IN (
        SELECT TRIM(movement_id)
        FROM raw_inventory_movements
        WHERE TRIM(COALESCE(movement_id, '')) != ''
        GROUP BY TRIM(movement_id)
        HAVING COUNT(*) > 1
    )

    AND TRIM(COALESCE(product_id, '')) != ''

    AND date(movement_date) IS NOT NULL
    AND LENGTH(movement_date) = 10

    AND UPPER(TRIM(movement_type)) IN ('IN', 'OUT')

    AND CAST(quantity AS INTEGER) > 0

    AND CAST(unit_cost AS REAL) > 0;


-- 3. Create an analytical inventory summary.

CREATE TABLE inventory_summary AS

SELECT
    product_id,
    product_name,
    category,
    warehouse_id,

    SUM(signed_quantity) AS current_stock,

    SUM(
        signed_quantity * unit_cost
    ) AS net_movement_value

FROM clean_inventory_movements

GROUP BY
    product_id,
    product_name,
    category,
    warehouse_id;
