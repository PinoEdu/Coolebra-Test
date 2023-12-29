import psycopg2
from functions import insertValues, createTables, insertQuery

def firstQuery(cur):
    cur.execute("""
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
    """)

    rows = cur.fetchall()
    
    return rows


def agrupar(datos_productos):
    productos_agrupados = {}

    for nombre, valor_activo, ean, sku, mercado in datos_productos:
        if ean not in productos_agrupados:
            productos_agrupados[ean] = {
                'nombre_producto' : nombre,
                'datos_query' : [(nombre, valor_activo, ean, sku, mercado)],
                'cantidad_markets_diferentes' : sum(1 for row in datos_productos if ean == row[2]),
                'rango_precios' : (valor_activo, valor_activo)
            }
        else:
            productos_agrupados[ean]['datos_query'].append((nombre, valor_activo, ean, sku, mercado))
            productos_agrupados[ean]['rango_precios'] = (
                min(valor_activo,productos_agrupados[ean]['rango_precios'][0]),
                max(valor_activo,productos_agrupados[ean]['rango_precios'][1])
                )

    resultados_finales = []
    for ean, detalles in productos_agrupados.items():
        resultados_finales.append({
            'Ean': ean,
            'nombre_producto' : detalles['nombre_producto'],
            'datos_query' : detalles['datos_query'],
            'cantidad_markets' : detalles['cantidad_markets_diferentes'],
            'rango_precios' : detalles['rango_precios'][1] - detalles['rango_precios'][0]
        })

    return resultados_finales

try:
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'root'
    )

    print("Conexión exitosa")

    cur = conn.cursor()
    
    createTables(conn, cur) # Crea las tablas en caso de que no se hayan creado

    ###
    #insertValues(conn, cur)  # Poblamos las tablas creadas previamente solo una vez (para eso lo descomentamos)
    ###

    firstQuestion = firstQuery(cur)     # Pregunta 1
    agrupar(firstQuestion)              # Pregunta 3.a

    cur.close()

except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Conexión finalizada.")