def create_tables(conn, cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Product (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            sku VARCHAR(8) UNIQUE NOT NULL,
            ean VARCHAR(15) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Market (
            market_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Price (
            price_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES Product(product_id) ON DELETE CASCADE,
            market_id INT REFERENCES Market(market_id) ON DELETE CASCADE,
            normal_price INT NOT NULL,
            discount_price INT,
            active BOOLEAN NOT NULL,
            create_date DATE NOT NULL
        );
    """)

    conn.commit()

def poblar(conn, cur):
    cur.execute("""
        INSERT INTO Product (name, sku, ean) VALUES
            ('Producto A', 'SKU001', 'EAN001'),
            ('Producto B', 'SKU002', 'EAN002'),
            ('Producto C', 'SKU003', 'EAN003');
    """)

    cur.execute("""
        INSERT INTO Market (name) VALUES
            ('Mercado 1'),
            ('Mercado 2'),
            ('Mercado 3');
    """)

    cur.execute("""
        INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
            (1, 1, 100, 90, true, '2023-01-01');
    """)

    cur.execute("""
        INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
            (1, 2, 120, 110, true, '2023-01-01');
    """)

    cur.execute("""
        INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
            (2, 1, 80, 75, true, '2023-01-01');
    """)

    cur.execute("""
        INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
            (2, 3, 90, 85, true, '2023-01-01');
    """)

    cur.execute("""
        INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
            (3, 2, 50, 45, true, '2023-01-01');
    """)
    
    conn.commit()

def uniqueQuery(conn, cur):
    cur.execute("""
        INSERT INTO Price (product_id, market_id, normal_price, discount_price, active, create_date) VALUES
        (3, 3, 50, 49, true, '2023-02-01');
    """)

    conn.commit()