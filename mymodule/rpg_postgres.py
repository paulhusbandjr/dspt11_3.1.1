import psycopg2
import sqlite3
import pandas as pd
import os
import sqlalchemy

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

# setting up sqlite3 connection
sq_engine = sqlalchemy.create_engine('sqlite:///../rpg_db.sqlite3')
sq_con = sqlite3.connect('../rpg_db.sqlite3')
sq_curs = sq_con.cursor()

# creating lists of the original names, new names, and keys for the database migration
old_table_names = ['armory_item', 'armory_weapon', 'charactercreator_character',
                   'charactercreator_character_inventory', 'charactercreator_cleric',
                   'charactercreator_fighter', 'charactercreator_mage',
                   'charactercreator_necromancer', 'charactercreator_thief']

new_table_names = ['items', 'weapons', 'characters', 'inventories', 'clerics',
                   'fighters', 'mages', 'necromancers', 'thieves']

keys = ['item_id', 'item_ptr_id', 'character_id', 'id', 'character_ptr_id',
        'character_ptr_id', 'character_ptr_id', 'mage_ptr_id', 'character_ptr_id']

for i in range(len(old_table_names)):
    table = sq_curs.execute(""" select * from {}""".format(old_table_names[i]))
    table_df = pd.read_sql_table('{}'.format(old_table_names[i]), sq_engine)
    table_df.set_index(keys[i], inplace=True)
    if len(table_df) > 0:
        table_df.to_sql('{}'.format(new_table_names[i]), engine, if_exists='replace')

pg_conn.close()
sq_con.close()
