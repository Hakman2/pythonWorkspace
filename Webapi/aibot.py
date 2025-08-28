import requests

api_key = "55146be6397197536033ce9b2dd8e946"

def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant info
        lon = weather_data['coord']['lon']
        lat = weather_data['coord']['lat']
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        city = weather_data['name']
        country = weather_data['sys']['country']

        return {
            "city": city,
            "country": country,
            "lon": lon,
            "lat": lat,
            "weather": weather,
            "temp": temp
        }

    except requests.exceptions.RequestException:
        return {
            "error": f"Could not connect to the weather service. Please check your internet connection or verify the city name: {city_name}"
        }
