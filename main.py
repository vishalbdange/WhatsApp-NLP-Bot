# Utils
from pymongo import MongoClient
from utils.visualisation import student_progress
from utils.video import youtube
from.utils.sendMessage import send_message
from utils.quiz import quiz_bot
from utils.dialogflowQuery import dialogflow_query

# Extra imports
from pymongo import MongoClient

# import flask for setting up the web server
from flask import Flask, request

import os

# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()


# creating the Flask object
app = Flask(__name__)


# Mongo CLient
DATABASE_URL = os.environ['DATABASE_URL']
mongoClient = MongoClient(DATABASE_URL)
db = mongoClient["wcdatabase"]

quiz_time = False

@app.route('/reply', methods=['POST'])
def reply():
    print("HELLLLLOCOCOCOCOCO")
    message = request.form.get('Body').lower()
    workflow(message)
    
def workflow(message):
    if not quiz_time:
        response_df = dialogflow_query(message)
        
        if response_df.query_result.intent.display_name == 'Video':
            result_videos = youtube(response_df.query_result.query_text)
            for video in result_videos:
                send_message(video['url'],video['thumbnail'])
            return 
        
        if response_df.query_result.intent.display_name == 'Parent':
            # if response_df.query_result.parameters
            

        