import turtle

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("Turtle Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# --- Scores ---
score_a = 0
score_b = 0

# --- Paddles ---
def create_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1) # Makes the square a rectangle
    paddle.penup()
    paddle.goto(x_pos, 0)
    return paddle

paddle_a = create_paddle(-350)
paddle_b = create_paddle(350)

# --- Ball ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ball speed X
ball.dy = 0.2  # Ball speed Y

# --- Scoreboard ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# --- Movement Functions ---
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250: paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250: paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250: paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250: paddle_b.sety(y - 20)

# --- Key Bindings ---
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

# --- Main Game Loop ---
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and Bottom Border Bouncing
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Left and Right Goals
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1