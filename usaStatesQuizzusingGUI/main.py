import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cor)

df = pd.read_csv('50_states.csv')
all_states = df.state.to_list()
guessed_states = []

state_turtle = Turtle()
state_turtle.penup()
state_turtle.hideturtle()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_states)}/50",
                                    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = df[df['state'] == answer_state]
        x = state_data.x.item()
        y = state_data.y.item()
        state_turtle.goto(x, y)
        state_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))

print(f"You guessed {len(guessed_states)} states correctly!")

turtle.mainloop()
