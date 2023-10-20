import random as rd
class Question:

    def __init__(self, q_text, q_answer, incorrect_answer):
        self.text = q_text
        self.answer = q_answer
        self.options=incorrect_answer + [q_answer]
        rd.shuffle(self.options)
