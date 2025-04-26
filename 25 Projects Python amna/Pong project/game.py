import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)  # Stretch the paddle vertically
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)  # Stretch the paddle vertically
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  # Horizontal speed of the ball
ball.dy = 0.1  # Vertical speed of the ball

# Score Variables
left_score = 0
right_score = 0

# Display Score
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# Paddle Movement Functions
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 20)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        left_paddle.sety(y - 20)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        right_paddle.sety(y - 20)


screen.listen()
screen.onkey(left_paddle_up, "w")  # Move left paddle up with 'w'
screen.onkey(left_paddle_down, "s")  # Move left paddle down with 's'
screen.onkey(right_paddle_up, "Up")  # Move right paddle up with arrow key
screen.onkey(right_paddle_down, "Down")  # Move right paddle down with arrow key

# Main game loop
while True:
    screen.update()  # Update the screen manually

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #  (Top and Bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

   
    if (ball.xcor() > 340 and ball.xcor() < 350) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # Ball bounces off the right paddle

    if (ball.xcor() < -340 and ball.xcor() > -350) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # Ball bounces off the left paddle

    # Scoring
    if ball.xcor() > 390:  # Ball goes out of bounds on the right
        left_score += 1
        ball.goto(0, 0)
        ball.dx *= -1
        score_display.clear()
        score_display.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # Ball goes out of bounds on the left
        right_score += 1
        ball.goto(0, 0)
        ball.dx *= -1
        score_display.clear()
        score_display.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))

    if left_score == 5:
        score_display.clear()
        score_display.write("Left Player Wins!", align="center", font=("Courier", 24, "normal"))
        break

    if right_score == 5:
        score_display.clear()
        score_display.write("Right Player Wins!", align="center", font=("Courier", 24, "normal"))
        break
