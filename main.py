# Utils
from pymongo import MongoClient
from utils.visualisation import student_progress
from utils.video import youtube
from utils.sendMessage import send_message
# from utils.quiz import quiz_bot
from utils.dialogflowQuery import dialogflow_query
from utils.webSearch import google_search
from api.text import sendText
from api.buttons import sendButtons

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

quiz_time = False

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
    quiz_bot2(db, 'M1', quiz_count)
    db['test'].update_one({ '_id':request.form.get('WaId') }, { "$set": { 'quiz_count': quiz_count }})
    print('COUNT ' + str(quiz_count))
    return ''
        

def quiz_bot2(db, quizID, questionNumber):
    collection = db["course"]
    quiz  = collection.find_one({ '_id': quizID })  
    questionNumberString = str(questionNumber)  
    if questionNumber > 0 and questionNumber < 6:
        # send_message(quiz[questionNumberString]['question'], '')
        # options = '\n' + quiz[questionNumberString]['A'] + '\n' + quiz[questionNumberString]['B'] + '\n' + quiz[questionNumberString]['C'] + '\n' + quiz[questionNumberString]['D'] + '\n'
        # send_message(options, '')
        sendButtons(request.form.get('WaId'), quiz, questionNumberString)
        
    if questionNumber > 1 and questionNumber < 7:
        questionNumberString = str(questionNumber - 1)  
        return quiz[questionNumberString]['answer']
    else:
        return ''

def quiz_chat(user, user_answer):
    global quiz_time
    quiz_count = user['quiz_count']
    quiz_count = quiz_count + 1
    db['test'].update_one({ '_id':request.form.get('WaId') }, { "$set": { 'quiz_count': quiz_count }})
    print(quiz_count)        
    previous_answer = quiz_bot2(db, 'M1', quiz_count)
    if user_answer == previous_answer:
        quiz_marks = user['quizzes']['M1'] + 2
        print(quiz_marks)
        db['test'].update_one({'_id':request.form.get('WaId')}, { "$set": { 'quizzes.M1': quiz_marks}})
    if quiz_count == 6 or quiz_count > 6:
        quiz_time = False
        db['test'].update_one({'_id':request.form.get('WaId') }, { "$set": { 'quiz_count': 0 }})
        sendText(request.form.get('WaId'), 'Your quiz is over!')
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
        message = request.form.get('Body').lower() # video on digimon
        response_df = dialogflow_query(message)
        
        if response_df.query_result.intent.display_name == 'Videos':
            result_videos = youtube(response_df.query_result.query_text)
            print(result_videos)
            for video in result_videos:
                sendText(request.form.get('WaId'), video['url'] + ' | ' + video['title'])
            return ''
        
        if response_df.query_result.intent.display_name == 'WebSearch':
            result_search = google_search(response_df.query_result.query_text)
            sendText(request.form.get('WaId'), result_search)
        
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
            print(request.form.get('From'))
            # send_message(request.form.get('From'), response_df.query_result.fulfillment_text,'')
            sendText(request.form.get('WaId'), response_df.query_result.fulfillment_text)
            
    return ''

if __name__ == '__main__':
    app.run(debug=False)