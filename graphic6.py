import turtle
import math
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Turtle")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- Player ---
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.setheading(90) # Point upwards
player.goto(0, -250)

# --- Enemy ---
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.goto(0, 250)
enemy_dx = 2 # Speed of enemy moving left/right

# --- Bullet ---
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 10
bullet_state = "ready" # "ready" means it can fire, "fire" means it's moving

# --- Functions ---
def move_left():
    x = player.xcor()
    if x > -280: player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280: player.setx(x + 20)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move bullet to just above the player
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# --- Keyboard Bindings ---
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# --- Main Game Loop ---
while True:
    screen.update()

    # Move the enemy
    enemy.setx(enemy.xcor() + enemy_dx)

    # Reverse enemy at borders
    if enemy.xcor() > 280 or enemy.xcor() < -280:
        enemy_dx *= -1
        enemy.sety(enemy.ycor() - 10) # Drop down slightly

    # Bullet movement logic
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + bullet_speed)

    # Check if bullet went off screen
    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet_state = "ready"

    # Collision detection
    if bullet.distance(enemy) < 20:
        # Reset enemy
        enemy.goto(random.randint(-200, 200), 250)
        # Reset bullet
        bullet.hideturtle()
        bullet_state = "ready"
        print("Hit!")

    # Check if enemy reached player (Game Over)
    if enemy.ycor() < -240:
        print("The Aliens Have Landed! Game Over.")
        break 