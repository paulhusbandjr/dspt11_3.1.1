from pymongo import MongoClient
import ssl
import os

# grab environment variables for mongo database
MONGO_DB_USER = os.getenv('MONGO_DB_USER')
MONGO_DB_PASS = os.getenv('MONGO_DB_PASS')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
mongo_client = MongoClient(
    f'mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASS}@cluster0.i2ija.mongodb.net/{MONGO_DB_NAME}?retryWrites=true&w=majority',
    ssl_cert_reqs=ssl.CERT_NONE)
mongo_db = mongo_client.myFirstDatabase
rpg = mongo_db.rpg

# queries
character_count = rpg.count_documents({})

# results
print("There are", character_count, "character records.")
