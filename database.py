import psycopg2
import time
import os
X = 1

while True:
    try:
        conn = psycopg2.connect(database="postgres",
                                user="postgres",
                                password="1",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        print('Connected to database')
        break
    except:
        time.sleep(1)
        continue

try:
    cursor.execute("CREATE SCHEMA shema;")
    print('Created schema')
except:
    print('Schema already exist')
    pass

try:
    cursor.execute("CREATE TABLE shema.table (frame TEXT, id TEXT, bbox_left TEXT,"
                   "bbox_top TEXT, bbox_w TEXT, bbox_h TEXT);")
    print('Created table shema.table')
    conn.commit()
except:
    print('Table already exist')
    pass
