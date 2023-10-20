import html


from question_model import Question
from data import get_new_question
from quiz_brain import QuizBrain
from ui import QuizInterface



question_bank = []
for question in get_new_question():
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    incorrect_answers = [html.unescape(x) for x in question["incorrect_answers"]]

    new_question = Question(question_text, question_answer, incorrect_answers)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

QuizInterface(quiz)
