# Note! For the code to work you need to replace all the placeholders with
# Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = 'OPEN-WEATHER_API_KEY'
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

lat = 'YOUR_LATITUDE'
lon = 'YOUR_LONGITUDE'

phone_no = 'YOUR_PHONE_NO'

response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}'
                        f'&exclude={"current,minutely,daily"}&appid={api_key}')
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:13]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                body=":It's Going To Rain Today."
                "Don't Forget Take Umbrella 🌂",
                from_='+12483318850',
                to=phone_no)
    print(message.status)
else:
    print('Clear Sky!')
