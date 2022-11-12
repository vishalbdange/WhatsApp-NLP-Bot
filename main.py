# Utils
import json
from pymongo import MongoClient

from utils.visualisation import student_progress
from utils.video import youtube
from utils.speech_to_text import speech_to_text
from utils.web_search import google_search
# Extra imports
from pymongo import MongoClient

# import flask for setting up the web server
from flask import Flask, request,Response

# import the Client function from the helper library
from twilio.rest import Client

# import Messaging Response for responding to incoming messages
from twilio.twiml.messaging_response import MessagingResponse

# import OS for environment variables
import os

#import requests to make API call
import requests

import langid


# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()

# import dialogflow for adding conversational AI
import dialogflow
from google.api_core.exceptions import InvalidArgument

from deep_translator import GoogleTranslator

# creating the Flask object
app = Flask(__name__)

# set Google Application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dialogflow_private_key.json' # absolute path of JSON file

# set Twilio user credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = os.environ['YOUR_WHATSAPP_NUMBER']
client = Client(account_sid, auth_token)

# set Dialogflow project credentials
DIALOGFLOW_PROJECT_ID = os.environ['DIALOGFLOW_PROJECT_ID']
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = os.environ['SESSION_ID']
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


#importing youtube Videos 


# Mongo CLient
# DATABASE_URL = os.environ['DATABASE_URL']
# mongoClient = MongoClient(DATABASE_URL)
# db = mongoClient["wcdatabase"]

def send_message(message_body,imageUrl):
    # send text message from bot to user
    text_message = client.messages.create(
        body=message_body,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919960855675',
        media_url=imageUrl
    )
def send_text_message(message_body):
# send text message from bot to user
    text_message = client.messages.create(
        body=message_body,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919960855675',
    )

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response )

@app.route('/reply', methods=['POST'])
def reply():
    print("HELLLLLOCOCOCOCOCO")
    
    message = request.form.get('Body').lower()
    print(request.form)
   

    # _______________________ Keval Code ______________________
    if message :
        print(message)
        translated = GoogleTranslator(source="auto", target="en").translate(message)
        print(translated)
        lang_code = langid.classify(message)[0]
        print(lang_code)
        text_input = dialogflow.types.TextInput(text=translated, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            print("Query text:", response.query_result.query_text)
            print("Detected intent:", response.query_result.intent.display_name)
            # print(response.query_result)
            # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
            # print("Fulfillment text:", response.query_result.fulfillment_text)
            # print(response.query_result.fulfillment_text)
            # index(response.query_result.query_text)

            # mediaUrl = student_progress(db)
            videos = youtube(response.query_result.query_text)
            for video in videos:
                video_flag = True
                send_message(video['url'],video['thumbnail'])
            # web_search_results = google_search(response.query_result.query_text)
            # send_text_message(GoogleTranslator(source="auto", target=lang_code).translate(response.query_result.fulfillment_text))
            # for result in web_search_results:
            #     send_text_message(result['snippet'] + '\n' + result['link'])
            return ""
        except InvalidArgument:
            raise