from tkinter import *
from quiz_brain import QuizBrain
from time import sleep
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain): #Definining the datatype is optional. Just did it so vs code could show me the methods
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        # Score
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1)


        # Question Bank
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question Here", width=290, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        # Answer Buttons
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):   
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.true_button["state"] = "normal"
            self.false_button["state"] = "normal"
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz!\nYour score is:\n{self.quiz.score}/{self.quiz.question_number}")




    def check_answer_true(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)



    def check_answer_false(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)


    def give_feedback(self, result):
        self.canvas.itemconfig(self.question_text, fill="white")
        if result:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        self.window.after(1000, self.get_next_question)
        

