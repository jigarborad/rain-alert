import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ddaff6767318a751c4503a5a070ddaab"
account_sid = "AC424a51e79399b615b41ad2da94d446f9"
auth_token = "2419fbe477dfa79ac1edc84f4427af05"


weather_params = {
    "lat": 41.763599,
    "lon": -2.464920,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client =  Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today",
        from_='+18482855433',
        to=,
    )
else:
    print("No need to bring an umbrella")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Its not going to rain today",
        from_='+18482855433',
        to='+49 17686072127',
    )