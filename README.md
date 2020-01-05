### check_vehicle.py

This script will check your Tesla vehicle and notify you when it is unplugged during off-peak hours.

 - Pulls Tesla stats via Teslafi.com
 - Sends SMS notifications using Twilio

#### How to use check_vehicle.py
1. Set your desired alert preferences at the top of the script
2. Set environment variables with your Twilio and Teslafi information
 `teslafi_api`: Teslafi API URL
 `twilio_sid`: Twilio account SID
 `twilio_token`: Twilio authentication token
 `twilio_sms_to`: Number to send notifications to (must be validated in Twilio)
 `sms_from`: Twilio phone number