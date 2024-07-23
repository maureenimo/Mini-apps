from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
MY_FONT = ("Times New Roman", 20)

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx= 20, pady= 20)

        self.label = Label(text=f"Score: 0", font=MY_FONT, bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.label.grid(column=1, row= 0)
        
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text='Text', fill=THEME_COLOR, font=MY_FONT, width=280)
        self.canvas.grid(column=0, row= 1, columnspan= 2, pady=30)
        
        right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right, highlightthickness=0, command=self.right_answer)
        self.right_button.grid(column = 0, row =2)
        
        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(column = 1, row =2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz. ") 
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            
    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
        