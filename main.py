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

def send_youtube_result(message_body,thumbnail):
    # send text message from bot to user
    text_message = client.messages.create(
        body=message_body,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919960855675',
        media_url=thumbnail
    )

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
    return str(response )

 
def get_youtube_results_for(query_text):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    videos = []

    search_params = {
        'key' : os.environ['YOUTUBE_API_KEY'],
        'q' : query_text,
        'part' : 'snippet',
        'maxResults' : 4,
        'type' : 'video'
    }

    r = requests.get(search_url, params=search_params)

    results = r.json()['items']

    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])


    video_params = {
        'key' : os.environ['YOUTUBE_API_KEY'],
        'id' : ','.join(video_ids),
        'part' : 'snippet,contentDetails',
        'maxResults' : 4
    }

    r = requests.get(video_url, params=video_params)
    results = r.json()['items']
 
    for result in results:
        video_data = {
            'id' : result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'thumbnail' : result['snippet']['thumbnails']['high']['url'],
            'duration' : 0,
            'title' : result['snippet']['title'],
        }
        videos.append(video_data)
        
    print(videos)
    for video in videos:
        send_youtube_result(video['url'],video['thumbnail'])


@app.route('/reply', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
 
    if message:
        text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
            print("Query text:", response.query_result.query_text)
            # print("Detected intent:", response.query_result.intent.display_name)
            # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
            # print("Fulfillment text:", response.query_result.fulfillment_text)

            get_youtube_results_for(response.query_result.query_text)
            return respond(response.query_result.fulfillment_text)
 
        except InvalidArgument:
            raise


