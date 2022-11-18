from api.twoButton import sendTwoButton
from api.text import sendText
from utils.dialogflowQuery import dialogflow_query


def trialFlow(request,db):
    #After Regstration i.e. Neel's Code

    user  = db['test'].find_one({ '_id':request.form.get('WaId') })
    if user == None:
        return ''
    print(user)
    message = request.form.get('Body')
    print(message)
    
    
    if(user['scheduleDone'] == 'false' and user['payment'] == 'false' and message == 'Reschedule the class'):
        print("Your trial class is booked successfully")
        # print("Calendly logic will come...")
        #After scheduleDone class , update scheduleDone true in db
        sendText(request.form.get('WaId'),"en","Your trial class is booked successfully!")
    elif(user['scheduleDone'] == 'false' and user['payment'] == 'false' and message == 'Go for Payment'):
        sendText(request.form.get('WaId'),"en","Sending you the payment link for the given course..." + 'localhost:5000/register-for-course/'+request.form.get('WaId')) 
        # db['test'].update_one({ '_id':request.form.get('WaId') }, { "$set": { "payment": 'true' } })
        print("Sending you the payment link for the given course..." + 'localhost:5000/register-for-course/'+ request.form.get('WaId'))
    elif(user['scheduleDone'] == 'false' and user['payment'] == 'false'):
        sendTwoButton(request.form.get('WaId'),"en",'Please select Any of the below options',["reschedule","payment"],['Reshedule the class','Go for Payment'])
    elif(user['scheduleDone'] == 'true' and user['payment'] == 'false' and message=='Yes'):
        sendText(request.form.get('WaId'),"en","Sending you the payment link ...")
        sendText(request.form.get('WaId'),"en","Sending you the payment link for the given course..." + 'https://vikings.onrender.com/register-for-course/'+ request.form.get('WaId')) 
        
        #After Payment Update the payment true in db
    elif(user['scheduleDone'] == 'true' and user['payment'] == 'false' and message=='No'): 
        sendText(request.form.get('WaId'),"en","Please Surf our other courses....")
        sendText(request.form.get('WaId'),"en","Catalgue Comes here....")
    elif(user['scheduleDone'] == 'true' and user['payment'] == 'false'): 
        sendTwoButton(request.form.get('WaId'),"en",'Do you want to Enroll in the course ?',['yes','no'],['Yes','No'])
   

    elif(user['scheduleDone'] == 'false' and user['payment'] == 'true' and message=="Yes"):
        sendText(request.form.get('WaId'),"en","Rescheduling your trial class... Find the below Calendly schedule..")
    elif(user['scheduleDone'] == 'false' and user['payment'] == 'true' and message=="No"):
        sendText(request.form.get('WaId'),"en","That's Okay... Happy Learning !")
    elif(user['scheduleDone'] == 'false' and user['payment'] == 'true'):
        #Access to resources
        #send message Drive link
        #This is your scheduleDone video/class
        print("scheduleDone False Pay true")
        sendText(request.form.get('WaId'),"en",'You have the access to all the resource such as Google your doubts, Watch videos ,Get notes')
        sendTwoButton(request.form.get('WaId'),"en",'Do you want to reschedule your pending scheduleDone class ?',['yes','no'],['Yes','No'])
        # sendText(request.form.get('WaId'),'en',"Do you want to take you scheduleDone class ?")

    elif(user['scheduleDone'] == 'true' and user['payment'] == 'true'):
        print("Heyy, How May I help you ?")
