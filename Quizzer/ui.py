from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


##GUI ##

class Quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.qsn = self.canvas.create_text(150, 125, width= 250, text="question will appear here", font=("Aerial",20,"italic"), fill=THEME_COLOR)

        self.score_lable = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lable.grid(column=1, row=0)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, width=100, height=97, highlightthickness=0, command=self.true_button_clicked)
        self.true_button.grid(column=1, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, width=100, height=97, highlightthickness=0, command= self.false_button_clicked)
        self.false_button.grid(column=0, row=2)

        self.get_new_qsn()
        self.window.mainloop()

    def get_new_qsn(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_lable.config(text=f"score: {self.quiz.score}")
            next_qsn = self.quiz.next_question()
            self.canvas.itemconfig(self.qsn, text=next_qsn)

    def true_button_clicked(self):
        is_correct = self.quiz.check_answer("True")
        print(is_correct)
        self.give_feedback(is_correct)

    def false_button_clicked(self):
        is_correct = self.quiz.check_answer("False")
        print(is_correct)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_new_qsn)
