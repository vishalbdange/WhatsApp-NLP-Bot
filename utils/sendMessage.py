import os
from dotenv import load_dotenv
load_dotenv()

# import the Client function from the helper library
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = os.environ['YOUR_WHATSAPP_NUMBER']
client = Client(account_sid, auth_token)

def send_message(message_body,imageUrl):
    # send text message from bot to user
    if imageUrl == '':
        text_message = client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',
            to='whatsapp:+919820860959',
        )
    else:
        text_message = client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',
            to='whatsapp:+919820860959',
            media_url=imageUrl
        )