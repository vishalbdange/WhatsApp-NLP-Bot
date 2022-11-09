# Utils
from pymongo import MongoClient
from utils.visualisation import student_progress
from utils.video import youtube
from utils.sendMessage import send_message
from utils.quiz import quiz_bot
from utils.dialogflowQuery import dialogflow_query

# Extra imports
from pymongo import MongoClient
import datetime

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

quiz_time = True

@app.route('/', methods=['POST'])
def reply():
    global quiz_time
    user  = db['test'].find_one({ '_id':request.form.get('WaId') })
    quiz_count = user['quiz_count']
    print("HELLLLLOCOCOCOCOCO")
    # message = request.form.get('Body').lower()
    if quiz_time and quiz_count == 0:
        quiz_initial(user, quiz_count)
        return ''

    workflow(request)
    return ''
    
def quiz_initial(user, quiz_count):
    quiz_count = quiz_count + 1
    quiz_bot(db, 'M1', quiz_count)
    db['test'].update_one({ '_id':request.form.get('WaId') }, { "$set": { 'quiz_count': quiz_count }})
    print('COUNT ' + str(quiz_count))
    return ''
        

def quiz_chat(user, user_answer):
    global quiz_time
    quiz_count = user['quiz_count']
    quiz_count = quiz_count + 1
    db['test'].update_one({ '_id':request.form.get('WaId') }, { "$set": { 'quiz_count': quiz_count }})
    print(quiz_count)        
    previous_answer = quiz_bot(db, 'M1', quiz_count)
    if user_answer == previous_answer:
        quiz_marks = user['quizzes']['M1'] + 2
        print(quiz_marks)
        db['test'].update_one({'_id':request.form.get('WaId')}, { "$set": { 'quizzes.M1': quiz_marks}})
    if quiz_count == 6 or quiz_count > 6:
        quiz_time = False
        db['test'].update_one({'_id':request.form.get('WaId') }, { "$set": { 'quiz_count': 0 }})
        send_message('Your quiz is over!','')
        return ''
    else:
        return ''

        

def workflow(request):
    global quiz_time
    if quiz_time:
        user = db['test'].find_one({ '_id':request.form.get('WaId') })
        quiz_answer = db['course']
        quiz_chat(user, request.form.get('Body'))
        return ''
        
    if not quiz_time:
        message = request.form.get('Body').lower()
        response_df = dialogflow_query(message)
        
        if response_df.query_result.intent.display_name == 'Videos':
            result_videos = youtube(response_df.query_result.query_text)
            print(result_videos)
            for video in result_videos:
                send_message(video['url'], video['thumbnail'])
            return ''
        
        if response_df.query_result.intent.display_name == 'Parent':
            print(response_df.query_result.parameters)
            picture_url = student_progress(db)
            send_message(response_df.query_result.fulfillment_text, picture_url)
            return ''
        
        else:
            # quiz_bot(db, 'M1')
            now = datetime.datetime.now()
            print(now.year, now.month, now.day, now.hour, now.minute, now.second)
            print(type(now.year), type(now.month), type(now.day), type(now.hour), type(now.minute), type(now.second))
            send_message(response_df.query_result.fulfillment_text,'')
            
    return ''