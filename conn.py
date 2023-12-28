import psycopg2

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'root'
    )

    print("Conexión exitosa")

    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    
    row = cursor.fetchone()
    print(row)

    ##cursor.execute("SELECT * FROM ...")
    ##rows = cursor.fetchall()
    ##for row in rows:
    ##    print(row)

except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada.")