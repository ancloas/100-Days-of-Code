from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []

for data in question_data:
    Question_Bank.append(Question(data['question'], data['correct_answer']))

quiz1=QuizBrain(Question_Bank)
while(not quiz1.is_end()):
    quiz1.ask_question()
    print('\n\n')


