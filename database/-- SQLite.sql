-- SQLite
SELECT
    movement_id,
    rejection_reason
FROM rejected_inventory_movements;

SELECT *
FROM clean_inventory_movements;

SELECT *
FROM inventory_summary
ORDER BY current_stock DESC;

SELECT *
FROM rejected_inventory_movements;

