import psycopg2
from functions import poblar, create_tables, uniqueQuery

def query(cur):
    cur.execute("""
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
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

try:
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'root'
    )

    print("Conexión exitosa")

    cur = conn.cursor()
    
    create_tables(conn, cur) # Crea las tablas en caso de que no se hayan creado

    ###
    #poblar(conn, cur)  # Poblamos las tablas creadas previamente solo una vez (para eso lo descomentamos)
    ###

    query(conn, cur)    # Pregunta 1

    cur.close()

except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Conexión finalizada.")