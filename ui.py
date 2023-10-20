from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain 
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.score=0
        self.quiz= quiz
        self.window= Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label=Label(text='Score: 0', background=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)
        self.question_canvas= Canvas(width=300, height=250, bg='white')
        self.question_text = self.question_canvas.create_text(150, 125, width=280, text="This is the first questi adsfsad a dsf asdfsd ad asdfas adfon", font=("Arial", 20, 'italic'))
        self.question_canvas.grid(column=0, row=1, columnspan=2)
        Img_true=PhotoImage(file='./images/true.png')
        self.button_true = Button(image=Img_true, command=self.chosen_true)
        self.button_true.grid(column=1, row=2)

        Img_false=PhotoImage(file='./images/false.png')
        self.button_false = Button(image=Img_false, command=self.chosen_false)
        self.button_false.grid(column=0, row=2)
        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        #reset canvas
        self.question_canvas.config(bg='white')
        #update score
        self.score_label.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            self.question_canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            messagebox.showinfo("Finished!!", f"You Have completed the quiz, Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.question_canvas.itemconfig(self.question_text, text="FINISHED")
            self.button_true.config(state='disabled')
            self.button_false.config(state='disabled')
            

    def chosen_true(self):
        if(self.quiz.check_answer('true')):
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')
        self.window.after(400, self.get_next_question)

        
    def chosen_false(self):
        if(self.quiz.check_answer('false')):
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')
        self.window.after(400, self.get_next_question)
        
