import turtle
import pandas

score = 0
guessed_states = []

state = turtle.Turtle()
state.color("Black")
state.penup()
state.hideturtle()

screen = turtle.Screen()
screen.title("U.S. States Game")


#importing US state image"
image = "blank_states_img.gif"  
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


# playing loop until we guess all 50 states #
while score != 50:
    user_guess = screen.textinput(title= f"{score}/50 Guessed states", prompt="What's another state name?").title()

    if user_guess == "Exit":
        break

    if user_guess in all_states:
        print(user_guess)
        guessed_states.append(user_guess)
        state.goto(int(data[data.state == user_guess].x), int(data[data.state == user_guess].y))
        state.write(user_guess, align='center', font=("Aerial", 12, "normal"))
        score += 1
        
# listing all states which user has not been able to guess ##
states_to_learn = set(all_states) ^ set(guessed_states)
detail = pandas.DataFrame(states_to_learn)
detail.to_csv("States_to_learn.csv")


