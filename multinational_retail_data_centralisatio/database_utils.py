import os
import psycopg2
import yaml
from sqlalchemy import create_engine
import pandas as pd
# import db_creds.yaml

class DatabaseConnector:
    def __init__(self):
        self.engine = self.init_db_engine()
        self.credentials = self.read_db_creds()

    def read_db_creds(self):
        file_path = os.path.join(os.path.dirname(__file__), 'db_creds.yaml')
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    
    def init_db_engine(self):
        engine = create_engine(f"{self.credentials['DATABASE_TYPE']}+{DBAPI}://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}")
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()

    def list_db_tables(self):
        # with self.engine.connect() as connection:
        #     result = connection.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        #     tables = [row[0] for row in result]
        #     return tables
        
        with psycopg2.connect(host=self.credentials['RDS_HOST'], user=RDS_USER, password=RDS_PASSWORD, dbname=RDS_DATABASE, port=RDS_PORT) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT table_name FROM information_schema.tables
                WHERE table_schema = 'public'""")
                for table in cur.fetchall():
                    print(table)
                return cur.fetchall()

