import os

import sqlite3 as sql
from datetime import datetime
from hashlib import md5

import polars as pl

from utils.paths import MODULE_PATH

class DataBase():

    def __init__(self):

        self.db_path = os.path.join(MODULE_PATH,"database", "database.db")
        self.connection_string = 'sqlite://' + "database/database.db"
        
        with sql.connect(self.db_path) as conn:
            pass

    
    def create_schema(self):

        schema_sql = open(os.path.join(MODULE_PATH,"database", "schema.sql")).read()
        
        with sql.connect(self.db_path) as conn:
            conn.executescript(schema_sql)
            conn.commit()

    
    def insert_event(self, event_name:str, event_date_time: datetime):
        event_id = md5(event_name.encode() + str(datetime.now()).encode()).hexdigest()

        sql_script = """INSERT INTO events VALUES (?, ?, ?)"""
        params = (event_id, event_name, event_date_time)

        with sql.connect(self.db_path) as conn:
            conn.execute(sql_script, params)
            conn.commit()


    def get_events(self):
        return pl.read_database_uri("select * from events", self.connection_string).to_dicts()


if __name__ == "__main__":

    db = DataBase()
    db.create_schema()

    db.insert_event(event_name = "my event", event_date_time = datetime(2024, 1, 1, 12, 0, 0))
    db.get_events()