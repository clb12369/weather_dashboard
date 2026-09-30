import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY")


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]

    return filtered_data



if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))