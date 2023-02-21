from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from enemy import EnemyAI

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

is_after_collision = False

p_paddle = Paddle((350, 0))
ball = Ball()
sb = Scoreboard()

is_input_ready = False
while is_input_ready == False:
    level = input("Input E for Easy, M for Medium, H for Hard, and I for Impossible")
    if level == "E":
        ai_paddle = EnemyAI((-350, 0), "Easy")
        is_input_ready = True

    elif level == "M":
        ai_paddle = EnemyAI((-350, 0), "Medium")
        is_input_ready = True

    elif level == "H":
        ai_paddle = EnemyAI((-350, 0), "Hard")
        is_input_ready = True

    elif level == "I":
        ai_paddle = EnemyAI((-350, 0), "Impossible")
        is_input_ready = True

    else:
        print("Please input E, M, H, or I")
        is_input_ready = False

def go_up():
    new_y = p_paddle.ycor() + 20
    p_paddle.goto(p_paddle.xcor(), new_y)

def go_down():
    new_y = p_paddle.ycor() - 20
    p_paddle.goto(p_paddle.xcor(), new_y)

def ai_movement(after_collision):
    if after_collision:
        if ball.ycor() < ai_paddle.ycor():
            ai_paddle.move_down()

        if ball.ycor() > ai_paddle.ycor():
            ai_paddle.move_up()

    else:
        pass

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball_position = ball.ycor()
    ai_movement(is_after_collision)

    sb.audio()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(p_paddle) < 50 and ball.xcor() > 320:
        is_after_collision = True
        ball.bounce_x()

    if ball.distance(ai_paddle) < 50 and ball.xcor() < -320:
        is_after_collision = False
        ball.bounce_x()
    
    if ball.xcor() > 380:
        is_after_collision = True
        ball.reset_position()
        sb.enemy_point()

    if ball.xcor() < -380:
        is_after_collision = False
        ball.reset_position()
        sb.player_point()


screen.exitonclick()
