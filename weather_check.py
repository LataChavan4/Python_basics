import requests
API = "https://api.openweathermap.org/data/2.5/weather"  ## UPI to get weather data ###
KEY = "fbd3cfa6f04c0cb662f18301dd06905a"
weather_parameters={
"lat": "Your location",
"lon":"Your location",
"appid":KEY,
}

## getting weather details from API ##
response = requests.get(API, params=weather_parameters)
response.raise_for_status()
print(response.status_code)
data= response.json()
print(data)
if int(data["weather"][0]['id']) < 700:
    print("Bring an umbrella")
