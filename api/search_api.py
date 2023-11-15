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

def search_movies(url, choice=None):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            parsed_data = json.loads(data)
            results = parsed_data.get('results')
            if results:
                details = []
                for result in results:
                    if choice:
                        chosen_attributes = []
                        if 'overview' in choice.lower():
                            chosen_attributes.append(result.get('overview'))
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
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

def search_tv_shows(url,  choice=None):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            parsed_data = json.loads(data)
            results = parsed_data.get('results')
            if results:
                details = []
                for result in results:
                    if choice:
                        chosen_attributes = []
                        if 'origin_country' in choice.lower():
                            chosen_attributes.append(result.get('origin_country'))
                        if 'overview' in choice.lower():
                            chosen_attributes.append(result.get('overview'))

                        if chosen_attributes:
                            details.append(chosen_attributes)
                        elif choice.lower() == 'all':  
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
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
