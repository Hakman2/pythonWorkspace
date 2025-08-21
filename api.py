import requests
import pprint
#API <--- Learning
api_key = "55146be6397197536033ce9b2dd8e946"
city_name = 'accra'

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

try:
        response = requests.get(url)
    # when going, when you encounter an error, tell us the error
        response.raise_for_status()
        # pprint.pprint(response.json())
        weather_data = response.json()
        # print(weather_data)

except requests.exceptions.RequestException:
        pprint.pprint(f"Could not connect to the weather service or please check your network/internet connecetion or check the name of the city, {city_name}")

coord = weather_data['coord']['lon']['lat']
print(coord)