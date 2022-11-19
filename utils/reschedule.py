# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()

from utils.db import db
from api.text import sendText
from api.twoButton import sendTwoButton
from datetime import date, timedelta

def rescheduleAppointment(intent, userWAId, langId, time):
    
    if intent == 'Schedule - time - no':
        sendText(userWAId, langId, "Okay! Your appointment timing remains untouched! See you then!")
        return ''
    
    if intent == 'Schedule - time - yes':
        tomorrow_ = date.today() +  timedelta(1)
        tomorrow = tomorrow_.strftime("%Y-%m-%d")
        free = db["appointments"].find_one({
            '_id': tomorrow,
            time: None
        })
        print(free)
        if free is not None:

            bookedTime = ''

            tomorrowSchedule = db["appointments"].find_one({
                '_id': tomorrow
            })

            for key in tomorrowSchedule.keys():
                if tomorrowSchedule[key] == userWAId:
                    bookedTime = key
                    break

                
                
            updated = db["appointments"].update_one({ '_id': tomorrow }, { "$set": { time: userWAId, bookedTime: None }} )
            if updated:
                print('Appointment scheduled')
                sendText(userWAId, langId, "Your appointment for tomorrow has been scheduled at " + time )
                return ''
            else:
                print('An erroneous response')
                sendText(userWAId, langId, "Please try again, an error occurred")
                return ''

        else:
            print('Time Slot unavailable')
            sendText(userWAId, langId, "Time slot unavailable")
            return ''
    else:
        sendText(userWAId, langId, "There seems to be a problem on our side, please try again later.")
        return ''