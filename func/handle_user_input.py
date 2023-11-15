from func.get_analytics_data import get_analytics_data
from func.print_analytics_data import print_analytics_data
from func.generate_bot_response import generate_bot_response
from db.db import connect_to_mongodb
import datetime

# Mongo DB connection
client, db, collection, analytics_collection = connect_to_mongodb()

# Function to handle user input
def handle_user_input(user_input, conversation_history):
    if user_input.lower() in ['exit', 'q', 'quit']:
        return False  # Signal to exit the conversation loop

    elif user_input.lower() == 'analytics':
        try:
            analytics_data = get_analytics_data()
            if analytics_data:
                print_analytics_data(analytics_data)
                print(analytics_data)
        except AttributeError as attr_err:
            print(f"An unexpected error occurred while fetching analytics data: {attr_err}")
        except Exception as e:
            print(f"An unexpected error occurred during analytics: {e}")
        return True
        

    else:
        bot_response = generate_bot_response(user_input, conversation_history)
        if bot_response == "Invalid choice. Please specify 'movies' or 'tv shows' to fetch data.":
            print(bot_response) 
            return True  # Continue the conversation loop

        print("Bot:", bot_response)
        
        conversation = {
            "user_input": user_input,
            "bot_response": bot_response,
            "timestamp": datetime.datetime.now()
        }
        collection.insert_one(conversation)
        conversation_history.append(conversation)
        return True

