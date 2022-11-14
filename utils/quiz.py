from utils.sendMessage import send_message
from api.quizButtons import sendQuiz

def quiz_bot(db, quizID, questionNumber):
    collection = db["course"]
    quiz  = collection.find_one({ '_id': quizID })  
    questionNumberString = str(questionNumber)  
    if questionNumber > 0 and questionNumber < 6:
        # send_message(quiz[questionNumberString]['question'], '')
        # options = '\n' + quiz[questionNumberString]['A'] + '\n' + quiz[questionNumberString]['B'] + '\n' + quiz[questionNumberString]['C'] + '\n' + quiz[questionNumberString]['D'] + '\n'
        # send_message(options, '')
        sendQuiz()
        
    if questionNumber > 1 and questionNumber < 7:
        questionNumberString = str(questionNumber - 1)  
        return quiz[questionNumberString]['answer']
    else:
        return ''