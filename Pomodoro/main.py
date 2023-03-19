from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 0
timer_mech = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset ():
    window.after_cancel(timer_mech)
    Timer_lable.config(text="Timer")
    canvas.itemconfig(timer, text="00:00")
    global rounds
    rounds = 0
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rounds
    checks = ""
    rounds +=1
    print(rounds)
    if rounds % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        Timer_lable.config(text="Break")
    elif rounds % 2 == 0:
        countdown(30)
        Timer_lable.config(text="Break")
    else:
        countdown(WORK_MIN*60)
        Timer_lable.config(text="Work")

    for i in range(math.floor(rounds/2)):
        checks += "✔"
        check_mark.config(text=checks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count<10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer, text=f"{min_count}:{sec_count}")

    if count>0:
        global timer_mech
        timer_mech = window.after(1000, countdown, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

## canvas needs to be created before adding image in screen ##
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

Timer_lable = Label(text="Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 20, "bold"))
Timer_lable.grid(column=1, row=0)

start_button = Button(text="start",command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label( bg=GREEN, fg= RED)
check_mark.grid(column=1, row=3)



window.mainloop()
