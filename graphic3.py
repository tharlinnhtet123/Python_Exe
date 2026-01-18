import turtle
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("The Great Turtle Race")

# Ask user for their bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? (red/orange/yellow/green/blue/purple): ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles with different colors
for index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    # Line them up at the start (left side of screen)
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

# --- Main Race Loop ---
while is_race_on:
    for turtle_racer in all_turtles:
        # Check if a turtle has crossed the finish line (x = 230)
        if turtle_racer.xcor() > 230:
            is_race_on = False
            winning_color = turtle_racer.pencolor()
            
            # Announce the winner
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        # Move each turtle a random distance
        rand_distance = random.randint(0, 10)
        turtle_racer.forward(rand_distance)

screen.exitonclick()