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

# def send_message(message_body):
#     # send text message from bot to user
#     text_message = client.messages.create(
#         body=message_body,
#         from_='whatsapp:+14155238886',
#         to='whatsapp:+91'+ 9960855675
#     )

@app.route('/message', methods=['GET', 'POST'])
def message():
    text_to_be_analyzed = "Cricket"
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise   

def respond(message):
    response = MessagingResponse()
    response.message(message)
    print(str(response))
    return str(response)

quiz_count = 0

@app.route('/reply', methods=['POST'])
def reply():
    global quiz_count
    message = request.form.get('Body').lower()
    print(request.form.get('WaId'))
    print('COUNT: ' + str(quiz_count) + ' for ' + request.form.get('WaId'))
    quiz_count += 1
    if message:
        text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            # print("Query text:", response.query_result.query_text)
            # print("Detected intent:", response.query_result.intent.display_name)
            # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
            # print("Fulfillment text:", response.query_result.fulfillment_text)
            print(response.query_result.fulfillment_text)
            return respond(response.query_result.fulfillment_text)
        except InvalidArgument:
            raise
            # 
