from func.perform_sentiment_analysis import perform_sentiment_analysis
from func.perform_topic_modeling import perform_topic_modeling
from func.calculate_user_engagement import calculate_user_engagement
import pymongo
from db.db import connect_to_mongodb

client, db, collection, analytics_collection = connect_to_mongodb()


# Function to perform analytics and store results in MongoDB
def perform_analytics():
    try:
            conversation_data = list(collection.find({}, {"_id": 0}))

            num_user_inputs = sum(1 for item in conversation_data if 'user_input' in item)
            num_bot_responses = sum(1 for item in conversation_data if 'bot_response' in item)

            sentiment_scores = perform_sentiment_analysis(conversation_data)

            prevalent_topics = perform_topic_modeling(conversation_data)

            engagement_metrics = calculate_user_engagement(conversation_data)

            analytics_result = {
                "total_user_inputs": num_user_inputs,
                "total_bot_responses": num_bot_responses,
                "sentiment_scores": sentiment_scores,
                "prevalent_topics": prevalent_topics,
                "engagement_metrics": engagement_metrics,
                "conversation_data": conversation_data
            }

            analytics_collection.insert_one(analytics_result)
            print("Analytics performed and results stored successfully.")

    except pymongo.errors.PyMongoError as e:
        print(f"MongoDB error occurred: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred during analytics: {ex}")
