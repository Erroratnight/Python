#First Lets the How the Class is generated?
#its Same as a function, "class" Keyword is used.
# An Initial Constructor is used and after decleration of each method it contains self attribute.


class Quiz():

    #Initilizer contains the initial attribute.
    def __init__(self,question_list):
        self.question_no = 0
        self.score=0
        self.question_list=question_list

    #Here its Checked that the number of question is less or More
    #if Less then only its will be Continued or else it is terminated.
    def more_question(self):
        return self.question_no < len(self.question_list)

    #Next question returns the next question from the list.
    #Its is also responsible for Mintaining the question number and incrementing it.
    #The question is printed on users screen.
    def next_question(self):
        current_question=self.question_list[self.question_no]
        Correct_Answer=current_question.answer
        self.question_no+=1
        Answer=input(f"Q.{self.question_no} {current_question.question} (True/False)?")
        self.check_answer(Answer,Correct_Answer)


    #After the user entered the Answer it is Checked by the below method,
    #It also maintain Correct answer and increment it whenever user enterd correct answer.
    def check_answer(self,Answer,Correct_Answer):
        self.Answer=Answer
        self.Corr=Correct_Answer
        if self.Answer.lower()==self.Corr.lower():
            self.score+=1
            print("Correct")
        else:
            print("Wrong")
        print(f"Correct answer is {self.Corr}")  #After user Entered Answer MAchine Also Display its answer
        print(f"Your Score is {self.score}/{self.question_no}") #Finally Score is printed at the end of each question.
        print("\n")