SELECT
    p.name,
    pr.normal_price,
    p.ean,
    p.sku,
    m.name AS market
FROM Product p
JOIN Price pr ON p.product_id = pr.product_id
JOIN Market m ON pr.market_id = m.market_id
WHERE pr.active = TRUE
ORDER BY pr.create_date DESC, pr.normal_price - COALESCE(pr.discount_price, 0) ASC
