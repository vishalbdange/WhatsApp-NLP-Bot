# my stuff
from typing import Dict
from dialogflow_fulfillment import Image, WebhookClient
from pymongo import MongoClient

# import flask for setting up the web server
from flask import Flask, request

# import the Client function from the helper library
from twilio.rest import Client

# import Messaging Response for responding to incoming messages
from twilio.twiml.messaging_response import MessagingResponse

# import OS for environment variables
import os

# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()

# import dialogflow for adding conversational AI
import dialogflow
from google.api_core.exceptions import InvalidArgument


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


def send_message(message_body):
    # send text message from bot to user
    text_message = client.messages.create(
        body=message_body,
        from_='whatsapp:+14155238886',
        to='whatsapp:+91'+phone_number
    )

# @app.route('/message', methods=['GET', 'POST'])
# def message():
#     text_to_be_analyzed = "Cricket"
#     text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
#     query_input = dialogflow.types.QueryInput(text=text_input)
#     try:
#         response = session_client.detect_intent(session=session, query_input=query_input)
#     except InvalidArgument:
#         raise   

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

def handler_df(agent_df: WebhookClient) -> None:
    agent_df.add('How are you feeling today?')

@app.route('/reply', methods=['POST'])
def reply():
    print("HELLLLLOCOCOCOCOCO")
    message = request.form.get('Body').lower()
    
    DATABASE_URL = os.environ['DATABASE_URL']
    myclient = MongoClient(DATABASE_URL)
    
    db = myclient["wcdatabase"]
    collection = db["test"]
    records = {
        "record":{
            "_id": 10,
            "name": "Dange",
            "Roll No": "201080909",
            "Branch": "IT",
        }
    }
    
    for record in records.values():
        collection.insert_one(record)
    
    
    # print(request)
    # res = request.get_json(force=True)
    # print("INNINININ")
    # print(res)
    # print(request.headers)
    # agent_df = WebhookClient(request.headers)
    
    # agent_df.handle_request(handler_df)
    # image = Image('https://www.sekirothegame.com/content/dam/atvi/sekiro/about/TGA-logo.png')
    
    if message:
        text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            # print("Query text:", response.query_result.query_text)
            # print("Detected intent:", response.query_result.intent.display_name)
            # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
            # print("Fulfillment text:", response.query_result.fulfillment_text)
            return respond(response.query_result.fulfillment_text) 
        except InvalidArgument:
            raise