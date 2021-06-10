import os
from pymongo import MongoClient
import psycopg2
import ssl
import sqlalchemy

# grab environment variables for mongo database
MONGO_DB_USER = os.getenv('MONGO_DB_USER')
MONGO_DB_PASS = os.getenv('MONGO_DB_PASS')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
mongo_client = MongoClient(
    f'mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASS}@cluster0.i2ija.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority',
    ssl_cert_reqs=ssl.CERT_NONE)
mongo_db = mongo_client.myFirstDatabase
rpg = mongo_db.rpg

# setting up connection for elephant database
dbname = os.getenv('PG_DB')
user = os.getenv('PG_User')
password = os.getenv('PG_Password')
host = os.getenv('PG_Host')
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()
pg_engine = sqlalchemy.create_engine(
    'postgresql://sjbbgwtw:LzAMn4-VIsFWwxN8CB-Znu7oUkqIJpKw@kashin.db.elephantsql.com/sjbbgwtw'
)

# check for rpg_data within the mongo collection
if not 'rpg_data' in mongo_db.list_collection_names():
    mongo_db.create_collection('rpg_data')

# get the relevant data from the elephant instance
characters_query = """select character_id, name, level, exp, hp,
                      strength, intelligence, dexterity, wisdom
                      from characters"""
characters_data = pg_engine.execute(characters_query).fetchall()
item_query = """select character_id, item_id from inventories"""
item_data = pg_engine.execute(item_query).fetchall()

# loop through the character data
for c in characters_data:
    items = []
    weapons = []
    # build list of items in character inventory
    for i in item_data:
        if i[0] == c[0]:
            items.append(i[1])
            if i[1] >= 138:
                weapons.append(i[1])
    # create the doc to be inserted
    doc = {'_id': c[0], 'name': c[1], 'level': c[2], 'exp': c[3], 'hp': c[4],
           'strength': c[5], 'intelligence': c[6], 'dexterity': c[7], 'wisdom': c[8],
           'items': items, 'weapons': weapons}
    # insert the document
    rpg.insert_one(doc)
    # statement letting user know
    print("Document inserted correctly.")

# close connections
pg_conn.close()
pg_engine.dispose()
mongo_client.close()
