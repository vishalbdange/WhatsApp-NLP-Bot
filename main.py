#import the Client function from the helper library
from twilio.rest import Client

#import OS for environment variables
import os

# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()

#set the User credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = os.environ['YOUR_WHATSAPP_NUMBER']
client = Client(account_sid, auth_token)

def main():
    #send text message
    text_message = client.messages.create(
        body='Hello there! I am the WhatsApp Bot!!',
        from_='whatsapp:+14155238886',
        to='whatsapp:+91'+phone_number
    )

if __name__ == '__main__':
    main()