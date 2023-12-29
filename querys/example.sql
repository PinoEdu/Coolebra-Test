INSERT INTO Product (name, sku, ean) VALUES
    ('Producto A', 'SKU001', 'EAN001'),
    ('Producto B', 'SKU002', 'EAN002'),
    ('Producto C', 'SKU003', 'EAN003');

INSERT INTO Market (name) VALUES
    ('Mercado 1'),
    ('Mercado 2'),
    ('Mercado 3');

INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
    (1, 1, 100, 90, true, '2023-01-01');

INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
    (1, 2, 120, 110, true, '2023-01-01');

INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
    (2, 1, 80, 75, true, '2023-01-01');

INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
    (2, 3, 90, 85, true, '2023-01-01');

INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
    (3, 2, 50, 45, true, '2023-01-01');

INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
    (3, 2, 50, 48, true, '2023-02-01');