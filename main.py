from db.db import connect_to_mongodb
from func.perform_analytics import perform_analytics
from func.handle_user_input import handle_user_input

# Mongo DB connection
client, db, collection, analytics_collection = connect_to_mongodb()

# Function to conduct the conversation
def bot_conversation():
    conversation_history = []
    print('Welcome to conversation bot!')
    while True:
        user_input = input("You: ")
        continue_conversation = handle_user_input(user_input, conversation_history)
        if not continue_conversation:
            break

# Main execution
if __name__ == "__main__":
    try:
        bot_conversation()
        perform_analytics()
    except KeyboardInterrupt:
        print("\nConversation interrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
