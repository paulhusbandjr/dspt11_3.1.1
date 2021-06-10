import psycopg2
import pandas as pd
import sqlalchemy
import os
import sqlite3

# create engine for sqlalchemy
engine = sqlalchemy.create_engine(
    'postgresql://sjbbgwtw:LzAMn4-VIsFWwxN8CB-Znu7oUkqIJpKw@kashin.db.elephantsql.com/sjbbgwtw'
)

# setting up connection for elephant db
dbname = os.environ['PG_DB']
user = os.environ['PG_User']
password = os.environ['PG_Password']
host = os.environ['PG_Host']
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# connecting to the table on github for the passenger data
titanic_engine = sqlalchemy.create_engine('sqlite:///../titanic.csv')
titanic_conn = sqlite3.connect('../titanic.csv')
titanic_cursor = titanic_conn.cursor()

# read the data into a pandas dataframe, then export it to the elephant instance.
passenger_data = pd.read_csv('../titanic.csv')
create_table = passenger_data.to_sql('passengers', engine,
                                     if_exists='replace')

pg_conn.close()
titanic_conn.close()
