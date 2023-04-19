from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.qsn = self.canvas.create_text(150, 125, text="question will appear here", font=("Aerial",20,"italic"), fill=THEME_COLOR)
        score_lable = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        score_lable.grid(column=1, row=0)

        true_image = PhotoImage(file="./images/true.png")
        true_button = Button(image=true_image, width=100, height=97, highlightthickness=0)
        true_button.grid(column=1, row=2)

        false_image = PhotoImage(file="./images/false.png")
        false_button = Button(image=false_image, width=100, height=97, highlightthickness=0)
        false_button.grid(column=0, row=2)

        self.window.mainloop()

    def get_new_qsn(self):
        next_qsn = self.quiz.next_question()
        self.canvas.itemconfig(self.qsn, text=next_qsn)

