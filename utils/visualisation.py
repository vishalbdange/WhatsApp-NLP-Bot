import os
from bson.objectid import ObjectId
import numpy as np
import matplotlib.pyplot as plt
from api.uploadMedia import uploadMedia 
from api.media import sendMedia
from utils.db import db
import pyimgur
import requests

# IMGUR client
IMGUR_CLIENT_ID = os.environ['IMGUR_CLIENT_ID']
imgurclient = pyimgur.Imgur(IMGUR_CLIENT_ID)

# ____________MatPlotLib & IMGUR Trial_____________
def studentProgress(receiver):
    collection = db["test"]
    student  = collection.find_one({ '_id': ObjectId("635a40cdcb5832c943b1804f")})
    student_marks = student["trial"]
    print(student_marks)
    
    plt.barh(["Quiz-1", "Quiz-2", "Quiz-3", "Quiz-4", "Quiz-5", "Quiz-6", "Quiz-7", "Quiz-8", "Quiz-9", "Quiz-10"], student_marks, align="center", label="Student Progress")
    plt.legend()
    plt.ylabel('Quizzes')
    plt.xlabel('Marks')
    plt.title('Progress of Student ID: {}'.format(student["_id"]))
    plt.savefig('studentplot.png')
    
    mediaId, mediaType = uploadMedia('studentplot.png', 'studentplot.png', 'png')
    print(mediaId, mediaType)
    sendMedia(receiver, mediaId, mediaType)
    
    # response = requests.get('https://i.imgur.com/ePhgVEA.jpg')
    # if response.status_code:
    #     fp = open('ytImage.jpg', 'wb')
    #     fp.write(response.content)
    #     fp.close()
    # mediaId,mediaType = uploadMedia('ytImage.jpg','ytImage.jpg','jpg')
    # sendMedia(receiver, mediaId, mediaType)
    
    # uploaded_image = imgurclient.upload_image('studentplot.png', title="Student Progress")
    # print(uploaded_image.link)
    # return uploaded_image.link
    