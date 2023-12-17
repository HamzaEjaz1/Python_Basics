# disctonary that stores question and answer
# have a varibale tackes the score of the palayes
# loop through th dictinary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz will completed


quiz ={
    "question1": {
        "Question": "What is the capital of Pakistan ?",
        "answer": "islamabad"
    },
    "question2": {"Question": "What is Nationl Dress of Pakistan?","answer": "shalwar qameez"
    },
    "question3": {
        "Question": "What is the Capital of Germany ?", "answer": "Berlin"
 }
}
score =0
for key, value in quiz.items():
    print(value['Question'])
    answer = input("Answer?")
    if answer.lower()== value['answer'].lower():
        print("correct")
        score=score+1
        print("Your Score is", str(score))
        print("")
        print("")
    else:
        print("wrong")
        print("The answer is :" + value['answer'])
        print("Your Score is :" + str(score))
        print("")
        print("")

print("you got "+str(score)+ " out of 3 question correctly")
print("you percentage is "+ str(score/3*100))