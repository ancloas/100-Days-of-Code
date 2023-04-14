
class Question:
    def __init__(self, text, answer ) -> None:
        self.text=text
        self.answer=answer
        
    def check_answer(self, ans):
        if ans.lower() == self.answer.lower():
            return True
        return False