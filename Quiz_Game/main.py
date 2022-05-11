#Quiz Game in Python CLI 
#Representation of Object Oriented Programming in Python
#Created by error_at_night
 # All Details are Mentioned in their Respected File.
from question import Question
from question_bank import Question_bank
from quiz import Quiz


#This is main file Which Controls the Entire Program.
question=[]

# The Below Loop Creates List of Question which Contains a pair of Question and answer.
for i in Question_bank:
    question_text=i["question"]
    question_answer=i["correct_answer"]
    Question1=Question(question_text,question_answer) 
    question.append(Question1)

#The Above loop refers to Question_bank from question_bank.
#Question_bank Contains all question and it is fetched and appended to question list.


# Now all Question are passed to Quiz Class in quiz.py 
#The Loop will Continue till the Question are available in question list
quiz=Quiz(question)
while quiz.more_question():
    quiz.next_question()


#The Final Ending Where , User Score is Displayed and the Final result is generated.

print("Conguratulaion You Have Completed the Quiz\n")
print(f"Your Score is: {quiz.score}/{quiz.question_no}\n")

if quiz.score>=((quiz.question_no//2)+1):
    print("You Passed The Quiz Test")
else:
    print("Sorry You Failed the Test")