from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")  # will change shape of cursor to turtle
timmy.color("gold1")   # will chnage color of cursor
timmy.forward(100)     # will move cursor in forward direction by given amount


myscreen = Screen()
print(myscreen.canvheight) # will print height of screen
myscreen.exitonclick() # will make sure taht screen gets closed after one click
