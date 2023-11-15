import urllib.request
import json
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}"
}

def get_all_content(url, choice=None):
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            parsed_data = json.loads(data)
            results = parsed_data.get('results')
            if results:
                details = []
                for result in results:
                    if choice and 'tv_shows' in choice.lower():
                        chosen_attributes = []
                        if 'name' in choice.lower():
                            chosen_attributes.append(result.get('name'))
                        if 'origin_country' in choice.lower():
                            chosen_attributes.append(result.get('origin_country'))
                        if 'overview' in choice.lower():
                            chosen_attributes.append(result.get('overview'))

                        if chosen_attributes:
                            details.append(chosen_attributes)
                        elif choice.lower() == 'all':  # Include 'all' attributes
                            details.append(result)
                    elif choice and 'movie' in choice.lower():
                        chosen_attributes = []
                        if 'title' in choice.lower():
                            chosen_attributes.append(result.get('title'))
                        if 'overview' in choice.lower():
                            chosen_attributes.append(result.get('overview'))
                        if 'release_date' in choice.lower():
                            chosen_attributes.append(result.get('release_date'))

                        if chosen_attributes:
                            details.append(chosen_attributes)
                        elif choice.lower() == 'all':  # Include 'all' attributes
                            details.append(result)
                    else:
                        details.append(result)

                if details:
                    formatted_results = json.dumps(details, indent=4)
                    return formatted_results
                else:
                    return "No results found."
            else:
                return "No results found."
    except urllib.error.HTTPError as e:
        return f'HTTPError: {e.code} {e.reason}'
    except urllib.error.URLError as e:
        return f'URLError: {e.reason}'

# Function to fetch all movies
def get_all_movies(url, choice=None):
    return get_all_content(url, choice)

# Function to fetch all TV shows
def get_all_tv_shows(url, choice=None):
    return get_all_content(url, choice)
