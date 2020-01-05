from twilio.rest import Client
from datetime import datetime
import time
import requests
import os

# getting api, auth, and phone info
url = os.environ['teslafi_api']
twilio_sid = os.environ['twilio_sid']
twilio_token = os.environ['twilio_token']
sms_to = os.environ['twilio_sms_to']
sms_from = os.environ['twilio_sms_from']

# setting the alert parameters
alert_after = "21:00:00"
alert_before = "23:00:00"
alert_battery = 50

# setting other variables
loop = 0

def check_tesla():
    # sending get request and saving the response as response object 
    r = requests.get(url = url)

    # extracting car data
    data = r.json()
    battery_percent = int(data['battery_level'])
    car_state = data['carState']
    car_name = data['vehicle_name']

    return [battery_percent, car_state, car_name]

def send_alert(battery_percent, car_name):
    # creating twilio client object
    client = Client(twilio_sid, twilio_token)
    # converting battery percent to string in order to concatenate
    battery_percent = str(battery_percent)

    # sending the alert
    message = client.messages.create(
        to=sms_to, 
        from_=sms_from,
        body=car_name+" is not plugged in! Current battery level: "+battery_percent
    )

    print(message.sid)

while loop == 0:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # checking if current time is within the specified alert window
    if current_time > alert_after and current_time < alert_before:
        battery_percent, car_state, car_name = check_tesla()
        if car_state != 'Charging' and battery_percent < alert_battery:
            # sending alert
            send_alert(battery_percent, car_name)
            # sleeping for 60 minutes
            time.sleep(3600)
        else:
            # sleeping for 30 minutes
            time.sleep(1800)
    else:
        # sleeping for 5 minutes
        time.sleep(300)