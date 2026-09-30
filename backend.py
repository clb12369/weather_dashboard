import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY")


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))