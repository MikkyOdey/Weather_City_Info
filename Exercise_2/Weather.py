import requests

# Enter your WeatherAPI key here
api_key = "41c9027a5f234f23be3123405262608 "

# Choose the city you want to check
city = "Lagos"

# Create the API request address
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# Send a request to the weather API
response = requests.get(url)

# Change the API response into Python data
weather_data = response.json()

# Get the temperature and weather condition
temperature = weather_data["current"]["temp_c"]
weather_condition = weather_data["current"]["condition"]["text"]

# Display the weather information
print("The city is", city)
print("The current temperature in the city is", temperature, "°C")
print("The weather condition in the city is", weather_condition)
