

class QuizBrain():
    def __init__(self, Question_list) -> None:
        self.question_no=0
        self.question_list=Question_list
        self.score=0


    def ask_question(self):
        ans= input(f"Q.{self.question_no+1}. {self.question_list[self.question_no].text} (True / False) ? ")
        #checking answer
        self.check_answer(ans)
        self.question_no+=1
           


    def check_answer(self, answer):
        is_correct= self.question_list[self.question_no].check_answer(answer)
        if is_correct:
            print('You got it right')
            self.score+=1            
        else:
            print('You got it wrong')
        print('The correct answer was: {}'.format(self.question_list[self.question_no].answer))
        print(f"Your current score is {self.score}/{self.question_no+1}")   
        
        return is_correct


    def is_end(self):
        if self.question_no>=len(self.question_list):
            print(f"The quiz is finished, your final score is:{self.score}/{self.question_no}")
            return True
        return False
    
