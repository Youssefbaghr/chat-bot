import pymongo
from dotenv import load_dotenv
import os

def connect_to_mongodb():
    # Load variables from .env file
    load_dotenv()

    # Retrieve variables from the environment
    mongo_db_str = os.getenv('MONGO_DB_STR')

    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_db_str)
    db = client["bot_db"]
    collection = db["conversations"]
    analytics_collection = db["analytics_data"]

    return client, db, collection, analytics_collection
