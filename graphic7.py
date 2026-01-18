import turtle
import random
import time

# --- Setup ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# --- Player ---
player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.setheading(90)
player.goto(0, -280)

def move_up():
    player.forward(20)

screen.listen()
screen.onkeypress(move_up, "Up")

# --- Car Management ---
COLORS = ["red", "purple", "blue", "green", "orange", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
cars = []
car_speed = STARTING_MOVE_DISTANCE

def create_car():
    # Only create a car 1 out of 6 times the loop runs to space them out
    if random.randint(1, 6) == 1:
        new_car = turtle.Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        cars.append(new_car)

# --- Main Loop ---
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    create_car()
    
    # Move cars
    for car in cars:
        car.backward(car_speed)
        
        # Detect Collision
        if car.distance(player) < 20:
            game_is_on = False
            msg = turtle.Turtle()
            msg.write("SQUASHED!", align="center", font=("Courier", 24, "bold"))

    # Detect Successful Crossing
    if player.ycor() > 280:
        player.goto(0, -280)
        car_speed += MOVE_INCREMENT # Level Up! Speed increases