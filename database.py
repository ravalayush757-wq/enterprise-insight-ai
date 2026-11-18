import sqlite3
import pandas as pd


class DatabaseManager:

    def __init__(self, db_name="database/business.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def load_dataframe(self, df, table_name="orders"):

        conn = self.connect()

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        print(f"Data successfully loaded into '{table_name}' table.")

    def execute_query(self, query):

        conn = self.connect()

        result = pd.read_sql(query, conn)

        conn.close()

        return result