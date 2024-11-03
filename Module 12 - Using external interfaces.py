# Exercise 1

import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json().get("value")
        print(joke)
    else:
        print("Failed to fetch a joke. Please try again.")

# Run the function
get_random_chuck_norris_joke()

# Exercise 2

import requests
import json

lat = 60
lon = 21
API_key = '53629cd97d95a4b8591741d1fb9c9809'
request_url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={API_key}"

try:
    response = requests.get(request_url)
    response.raise_for_status()

    weather = response.json()
    print("Response JSON:", json.dumps(weather, indent=2))

    if 'main' in weather and 'weather' in weather:
        print(f"""
            Location: Latitude {lat}, Longitude {lon}
            Temperature: {weather['main']['temp']}°C
            Weather: {weather['weather'][0]['description']}
            """)
    else:
        print("Unexpected response format. 'main' or 'weather' key is missing from the response.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server. Check your internet connection.")
except requests.exceptions.Timeout:
    print("Error: The request timed out. Try again later.")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
except KeyError as e:
    print(f"Unexpected response format. Missing key: {e}")
except Exception as e:
    print(f"An error occurred: {e}")