import turtle
import random
import time

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("Turtle Dodge Game")
screen.bgcolor("skyblue")
screen.setup(width=600, height=600)
screen.tracer(0) # Turns off animation for smoother movement

# --- Player Turtle ---
player = turtle.Turtle()
player.shape("turtle")
player.color("darkgreen")
player.penup()
player.goto(0, -250)

# --- Enemy ---
enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.goto(random.randint(-280, 280), 280)

# --- Score ---
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))

# --- Movement Functions ---
def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

# --- Keyboard Bindings ---
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# --- Main Game Loop ---
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    # Move the enemy down
    enemy.sety(enemy.ycor() - 5)

    # Check if enemy hit the bottom
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-280, 280), 280)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))

    # Collision detection (Distance between player and enemy)
    if player.distance(enemy) < 20:
        score_display.goto(0, 0)
        score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        game_is_on = False

screen.exitonclick()




