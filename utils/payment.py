# import flask for setting up the web server
from flask import *

# import OS for environment variables
import os

# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()

# import razorpay sdk
import razorpay
razorpay_key = os.environ['RAZORPAY_KEY_ID']
razorpay_secret = os.environ['RAZORPAY_KEY_SECRET']

from main import app
from utils.db import db
from api.text import sendText


@app.route('/register-for-course/<WaId>')
def form(WaId):
    global id, name
    global User_WaId
    User_WaId =  WaId
    print(User_WaId)
    id = 101 # from session
    name = 'Keval'  # from DB using id
    courses = ["10th", "12th", "JEE", "GRE"] # interested courses from database
    return render_template('payment_form.html', name=name, courses=courses, len=len(courses))

@app.route('/pay', methods=['POST'])
def pay():
    print(User_WaId)
    if request.method == "POST":
        global payment, course
        
        name = 'Keval'  # from DB using id
        email = 'keval@gmail.com' # from DB using id
        contact = os.environ['YOUR_WHATSAPP_NUMBER'] # from DB using id
        course = request.form['course']
        client = razorpay.Client(auth=(razorpay_key, razorpay_secret))
        notes = {
            'name': name,
            'email': email,
            'contact': contact,
            'course': course
        }
        payment = client.order.create({"amount": 15000, # from DB
            "currency": "INR",
            "payment_capture": 1,
            "notes": notes})
        return render_template('pay.html', payment=payment, razorpay_key=razorpay_key)


@app.route('/success', methods=['POST'])
def success():
    print(User_WaId)
    if request.method == "POST":
        print('Razorpay Payment ID: ' + request.form['razorpay_payment_id'])
        print('Razorpay Order ID: ' + request.form['razorpay_order_id'])
        print('Razorpay Signature: ' + request.form['razorpay_signature'])
        print(request.form)
        db['test'].update_one({ '_id': User_WaId}, { "$set": { "payment": 'true' } })
        print("Hi"+User_WaId + "Congratulations !! You are succefully register for this course !!")
        sendText(User_WaId,"en","COngratulations !! You are succefully register for this course !!")
        # get id and course from session and update payment status in database
        ## chatbot message for successful payment
        return '<h1> Payment Success </h1>'