
# ____________Mongo DB Insertion_____________

collection = db["test"]
records = {
    # "_id": 12,
    "name": "Karan",
    "Roll No": "1274849",
    "Branch": "IT",
    "quizzes": {
            "quiz-1": 6,
            "quiz-2": 4,
            "quiz-3": 10,
            "quiz-4": 3,
            "quiz-5": 7,
            "quiz-6": 8,
            "quiz-7": 1,
            "quiz-8": 5,
            "quiz-9": 2,
            "quiz-10": 9,
    },
    "trial": [7, 8, 3, 6, 1, 10, 9, 2, 4, 5]
}

# for record in records.values():
# collection.insert_one(records)
# print(records["_id"])

# ____________Mongo DB Updation_____________
# collection.update_one({ 'name': 'Shubham' }, { "$set": { 'Branch': 'CSE' }})
# collection.update_one({ '_id': ObjectId("635a3e93abe65112ae6dd603")}, { "$push": { 'trial': 100}})

# ____________Mongo DB Finding_____________
# result  = collection.find_one({ '_id': ObjectId("635a3e93abe65112ae6dd603") })
# print(result["quizzes"]['quiz-1'])
# quiz_marks = [result["quizzes"]['quiz-1'], result["quizzes"]['quiz-2']]
# print(quiz_marks)
# print(result["trial"])

# ____________Mongo DB Deletion_____________
# collection.delete_one({ 'name': 'Anshul'})
