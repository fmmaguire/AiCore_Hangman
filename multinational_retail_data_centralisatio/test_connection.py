import psycopg2
print('test')
with psycopg2.connect(host='data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com', 
    user='aicore_admin', 
    password='AiCore2022', 
    dbname='postgres', 
    port=5432
    ) as conn:

    with conn.cursor() as cur:
        cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
        for table in cur.fetchall():
            print(table)
