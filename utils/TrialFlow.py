from api.buttons import sendButtons_2
from api.text import sendText
from utils.dialogflowQuery import dialogflow_query


def trialFlow(request,db):
    #After Regstration i.e. Neel's Code
    user  = db['test'].find_one({ '_id':request.form.get('WaId') })
    print(user)
    message = request.form.get('Body')
    print(message)
    
    
    if(user['trial'] == 'false' and user['payment'] == 'false' and message == 'Reschedule the class'):
        print("Your Trial class is booked successfully")
        # print("Calendly logic will come...")
        #After trial class , update trial true in db
        sendText(request.form.get('WaId'),"Your Trial class is booked successfully!")
    elif(user['trial'] == 'false' and user['payment'] == 'false' and message == 'Go for Payment'):
        sendText(request.form.get('WaId'),"Sending you the payment link for the given course...")
        # db['test'].update_one({ '_id':request.form.get('WaId') }, { "$set": { "payment": 'true' } })
    
    elif(user['trial'] == 'false' and user['payment'] == 'false'):
        sendButtons_2(request.form.get('WaId'),'Please select Any of the below options',['Reshedule the class','Go for Payment'])
   
   
    elif(user['trial'] == 'true' and user['payment'] == 'false' and message=='Yes'):
        sendText(request.form.get('WaId'),"Sending you the payment link ...")
        sendText(request.form.get('WaId'),"Payment link : <payment_link>")
        #After Payment Update the payment true in db
    elif(user['trial'] == 'true' and user['payment'] == 'false' and message=='No'): 
        sendText(request.form.get('WaId'),"Please Surf our other courses....")
        sendText(request.form.get('WaId'),"Catalgue Comes here....")
    elif(user['trial'] == 'true' and user['payment'] == 'false'): 
        sendButtons_2(request.form.get('WaId'),'Do you want to Enroll in the course ?',['Yes','No'])
   
   
    elif(user['trial'] == 'false' and user['payment'] == 'true' and message=="Yes"):
        sendText(request.form.get('WaId'),"Rescheduling your trial class... Find the below Calendly schedule..")
    elif(user['trial'] == 'false' and user['payment'] == 'true' and message=="No"):
        sendText(request.form.get('WaId'),"That's Okay... Happy Learning !")
    elif(user['trial'] == 'false' and user['payment'] == 'true'):
        #Access to resources
        #send message Drive link
        #This is your trial video/class
        print("Trial False Pay true")
        sendText(request.form.get('WaId'),'You have the access to all the resource such as Google your doubts, Watch videos ,Get notes')
        sendButtons_2(request.form.get('WaId'),'Do you want to reschedule your pending trial class ?',['Yes','No'])
        # sendText(request.form.get('WaId'),"Do you want to take you trial class ?")

    elif(user['trial'] == 'true' and user['payment'] == 'true'):
        print("Heyy, How May I help you ?")
