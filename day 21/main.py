import turtle

import pandas

## Map Image
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## Logic
data = pandas.read_csv("50_states.csv")
states_guessed = []

states = data.state.to_list()

# while len(states_guessed) < 50:
## Player's interaction
guess = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
points = []

while len(points) < 50:
    if guess in states:
        points.append(guess)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        ##Here we wanto the state with the name witch the player has wrote, so in the data.state we wanto the guess and put this value on state_data
        state_data = data[data.state == guess]
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(state_data.state.item())

screen.exitonclick()
