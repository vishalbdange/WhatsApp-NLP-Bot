# import dotenv for loading the environment variables
from dotenv import load_dotenv
load_dotenv()

from db import db
from datetime import date

time_slots = {
    "5:00 PM": "17:00",
    "6:00 PM": "18:00",
    "7:00 PM": "19:00"
}

# https://www.mongodb.com/docs/atlas/app-services/triggers/scheduled-triggers/

def getTimeSlot(time):
    today = date.today().strftime("%Y-%m-%d")
    available = db["appointments"].find_one({
        '_id': today
    })
    res = [k for k,v in available.items() if v is None and k != '_id']
    return res

def bookTimeSlot(time, number):
    today = date.today().strftime("%Y-%m-%d")
    free = db["appointments"].find_one({
        '_id': today,
        time_slots[time]: None
    })
    print(free)
    if free is not None:
        updated = db["appointments"].update({
            '_id': today,
        }, {
            time_slots[time]: number
        })
        print(updated)
        return 'Appointment Scheduled'
    else:
        return 'Time Slot unavailable'