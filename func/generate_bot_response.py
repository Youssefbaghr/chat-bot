from dotenv import load_dotenv
from func.similarity import calculate_similarity
from func.preprocess_text import preprocess_text
import random
import os
from api.get_api import get_all_movies, get_all_tv_shows
from api.search_api import search_movies , search_tv_shows

# Load variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')

base_url = 'https://api.themoviedb.org/3'
get_movies = '/discover/movie'
get_tv_shows = '/discover/tv'
search_url_movies = '/search/movie?'
search_url_tv_shows = '/search/tv?'



# Function to generate bot responses based on user input
def generate_bot_response(user_input, conversation_history):
    if not conversation_history:
        return "Hello! How can I assist you?"

    last_input = conversation_history[-1]['user_input']
    last_response = conversation_history[-1]['bot_response']

    # Preprocess the inputs for comparison
    user_input_lower = preprocess_text(user_input.lower())
    last_input_lower = preprocess_text(last_input.lower())

    # Check for similarity in user queries
    similarity_threshold = 0.8
    if user_input_lower and last_input_lower:
        input_length = max(len(user_input_lower), len(last_input_lower))
        dynamic_threshold = min(similarity_threshold + (0.1 * input_length), 1.0)
        similarity = calculate_similarity(user_input_lower, last_input_lower)
        if similarity > dynamic_threshold:
            return "It seems you're asking about a similar topic again. Here are more details..."

    def generate_default_response():
        return "I'm sorry, I didn't quite understand that. How can I assist you?"

    # Map of predefined responses based on keywords
    responses = {
    "hello": ["Hi there! How can I help?", "Hello! What can I assist you with?"],
    "thanks": ["You're welcome!", "Glad I could help!"],
    "howareyou": ["I'm just a bot, but I'm here and ready to assist you!", "I'm here to help!"],
    "Ineedhelp": ["Sure, I'm here to help! What can I do for you?", "Of course! What do you need assistance with?"],
    "goodbye": ["Goodbye! Have a great day!", "Farewell! If you need anything else, feel free to ask."],
    "thanksgoodbye": ["You're welcome! Have a great day!", "Glad I could assist! Take care!"],
    "solvethis": ["Let me check that for you, please wait a moment.", "Sure, I'll look into it."],
    "writecode": ["That's an interesting question! Let me find the information for you.", "Sure, I'll get the details for you."]
    }

    user_keywords = ['hello', 'thanks', 'goodbye', "howareyou", "Ineedhelp", "solvethis", "writecode"]

    # Function to get appropriate response based on user keywords
    def get_response(user_input_keywords):
        if "hello" in user_input_keywords:
            return random.choice(responses["hello"])
        elif "thanks" in user_input_keywords:
            return random.choice(responses["thanks"])
        elif "goodbye" in user_input_keywords:
            return random.choice(responses["goodbye"])
        elif "howareyou" in user_input_keywords:
            return random.choice(responses["howareyou"])
        elif "Ineedhelp" in user_input_keywords:
            return random.choice(responses["Ineedhelp"])
        elif "solvethis" in user_input_keywords:
            return random.choice(responses["solvethis"])
        elif "writecode" in user_input_keywords:
            return random.choice(responses["writecode"])
    
    user_input_keywords = []
    for key in user_keywords:
        if key in user_input_lower:
            user_input_keywords.append(key)

    if user_input_keywords:
        bot_response = get_response(user_input_keywords)
        return bot_response
    elif "fetch" in user_input.lower() and ("movies" in user_input.lower() or "tv shows" in user_input.lower()):
        choice = ""

        if "movies" in user_input.lower():
            print("Available choices for attributes:")
            print("- title for movies (1)")
            print("- release_date for movies  (2)")
            print("- overview (3)")
            print("- all (for all available attributes)")
            choice = "movies"
            attribute_choice = input("Enter attribute choice: ")

            if attribute_choice.lower() == 'all':
                attribute_choice = None
            elif attribute_choice and attribute_choice.lower() not in ['1', '2', '3', '4', 'all']:
                return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
            else:
                # Map user input to corresponding attribute names
                mapping = {
                    '1': 'title',
                    '2': 'release_date',
                    '3': 'overview',
                    'all': None
                }
                attribute_choice = mapping.get(attribute_choice.lower(), None)

                if attribute_choice is None:
                    return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
                else:
                    attribute_choice = f"movies {attribute_choice}"
            url = f"{base_url}/{get_movies}?api_key={api_key}" if choice == "movies" else f"{base_url}/{get_tv_shows}?api_key={api_key}"
            
            data = get_all_tv_shows(url, attribute_choice) if choice == "tv_shows" else get_all_movies(url, attribute_choice)
            
            return data
        elif "tv shows" in user_input.lower():
            print("Available choices for attributes:")
            print("- name (1)")
            print("- origin_country (for TV shows) (2)")
            print("- overview (3)")
            print("- all (for all available attributes)")
            choice = "tv_shows"
            attribute_choice = input("Enter attribute choice: ")

            if attribute_choice.lower() == 'all':
                attribute_choice = None
            elif attribute_choice and attribute_choice.lower() not in ['1', '2', '3', '4', 'all']:
                return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
            else:
                # Map user input to corresponding attribute names
                mapping = {
                    '1': 'name',
                    '2': 'origin_country',
                    '3': 'overview',
                    'all': None
                }
                attribute_choice = mapping.get(attribute_choice.lower(), None)

                if attribute_choice is None:
                    return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
                else:
                    attribute_choice = f"tv_shows {attribute_choice}"
            url = f"{base_url}/{get_movies}?api_key={api_key}" if choice == "movies" else f"{base_url}/{get_tv_shows}?api_key={api_key}"
            data = get_all_tv_shows(url, attribute_choice) if choice == "tv_shows" else get_all_movies(url, attribute_choice)
            return data
        else:
            return "Invalid choice. Please specify 'movies' or 'tv shows' to fetch data."
    elif "search" in user_input.lower() and ("movies" in user_input.lower() or "tv shows" in user_input.lower()) :
        if "movies" in user_input.lower():

            print("Available choices for attributes:")
            print("- release_date for movies  (2)")
            print("- overview (3)")
            print("- all (for all available attributes)")
            choice = "movies"
            attribute_choice = input("Enter attribute choice: ")

            if attribute_choice.lower() == 'all':
                attribute_choice = None
            elif attribute_choice and attribute_choice.lower() not in [ '1', '2',  'all']:
                return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
            else:
                # Map user input to corresponding attribute names
                mapping = {
                    '1': 'release_date',
                    '2': 'overview',
                    'all': None
                }
                attribute_choice = mapping.get(attribute_choice.lower(), None)

                if attribute_choice is None:
                    return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
                else:
                    attribute_choice = f"movies {attribute_choice}"
            q = str(input('what movies you want to search : '))
            url =  f"{base_url}{search_url_movies}&query={q}"
            data = search_movies(url,attribute_choice)
            return data
        elif "tv shows" in user_input.lower():
            print("Available choices for attributes:")
            print("- overview (1)")
            print("- all (for all available attributes)")
            choice = "tv_shows"
            attribute_choice = input("Enter attribute choice: ")

            if attribute_choice.lower() == 'all':
                attribute_choice = None
            elif attribute_choice and attribute_choice.lower() not in [ '1',  'all']:
                return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
            else:
                # Map user input to corresponding attribute names
                mapping = {
                    '1': 'overview',
                    'all': None
                }
                attribute_choice = mapping.get(attribute_choice.lower(), None)

                if attribute_choice is None:
                    return "Invalid attribute choice. Please choose a valid attribute number or 'all'."
                else:
                    attribute_choice = f"tv_shows {attribute_choice}"
            q = str(input('what tv shows you want to search : '))
            url =  f"{base_url}{search_tv_shows}&query={q}"
            data = search_movies(url,attribute_choice)
            return data
        else:
            return "Invalid choice. Please specify 'movies' or 'tv shows' to fetch data."
    else : 
        return generate_default_response()

