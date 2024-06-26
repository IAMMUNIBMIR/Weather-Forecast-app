import requests

API_KEY = "2c766f42316bccfebc9d0af50b2387fd"


def getData(location,days=None):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)

    if not response:
        return {"error": "Location does not exist."}
    
    data = response.json()
    filtered_data = data["list"]
    numofval = 8 * days

    filtered_data = filtered_data[:numofval]
    
    return filtered_data


