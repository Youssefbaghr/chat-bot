import pymongo
from db.db import connect_to_mongodb

def get_analytics_data():
    try:
        # Establish MongoDB connection and get analytics collection
        client, db, collection, analytics_collection = connect_to_mongodb()
        
        # Check if collection is None or not connected
        if analytics_collection is None:
            print("Failed to establish MongoDB connection or collection is None.")
            return None
        else : 
            # Fetch analytics data from the collection
            analytics_data = list(analytics_collection.find({}, {"_id": 0}))
            return analytics_data

    except pymongo.errors.PyMongoError as e:
        print(f"Error retrieving analytics data: {e}")
        return None

    except AttributeError as ae:
        print(f"Attribute error occurred: {ae}")
        return None

    except Exception as ex:
        print(f"An unexpected error occurred while fetching analytics data: {ex}")
        return None
