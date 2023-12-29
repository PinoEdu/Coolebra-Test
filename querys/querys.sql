WITH PreciosRebajados AS (
    SELECT
        p.ean,
        p.sku,
        m.name as market,
        pr.normal_price - COALESCE(pr.discount_price, 0) AS precio_rebajado,
        pr.active,
        pr.create_date,
        ROW_NUMBER() OVER (PARTITION BY p.product_id ORDER BY pr.create_date DESC, pr.normal_price - COALESCE(pr.discount_price, 0) ASC) AS row_number
    FROM Product p
    JOIN Price pr ON p.product_id = pr.product_id
    JOIN Market m ON pr.market_id = m.market_id
    WHERE pr.active = true
)

SELECT
    precio_rebajado,
    ean,
    sku,
    market
FROM PreciosRebajados
WHERE row_number = 1;
