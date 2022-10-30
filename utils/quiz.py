from utils.sendMessage import send_message

def quiz_bot(db, quizID, questionNumber):
    collection = db["course"]
    quiz  = collection.find_one({ '_id': quizID })    
    send_message(quiz[questionNumber]['question'], '_')
    options = '\n' + quiz[questionNumber]['A'] + '\n' + quiz[questionNumber]['B'] + '\n' + quiz[questionNumber]['C'] + '\n' + quiz[questionNumber]['D'] + '\n'
    send_message(options, '_')
    return quiz[questionNumber]