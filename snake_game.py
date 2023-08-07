import turtle
import random
import time

# creating screen

screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("black")

# play_again = turtle.Turtle()
# play_again.speed(0)
# play_again.setup(width=70, height=50)
# play_again.bgcolor('black')
# play_again.goto(0, 0)
# play_again.write("play again \n", align="bottom", font=("courier", 38, "bold"))

# creating border

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score

score = 0;
delay = 0.1

snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('red')
food.penup()
food.goto(30, 30)

old_food = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('white')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("SCORE: ", align="center", font=("courier", 24, "bold"))


# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = 'up'


def snake_go_down():
    if snake.direction != "up":
        snake.direction = 'down'


def snake_go_right():
    if snake.direction != "left":
        snake.direction = 'right'


def snake_go_left():
    if snake.direction != "right":
        snake.direction = 'left'


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# keyboard binding

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # snake and food collisions
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {} ".format(score), align="center", font=("courier", 24, "bold"))
        delay -= 0.001


        # creating new food

        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("red")
        new_food.penup()
        old_food.append(new_food)

    for index in range(len(old_food) - 1, 0, -1):
        a = old_food[index - 1].xcor()
        b = old_food[index - 1].ycor()

        old_food[index].goto(a, b)

    if len(old_food) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a, b)

    snake_move()

    # snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("purple")
        scoring.goto(0, 0)
        scoring.write(" Game Over!!! \n Your Score is : {} ".format(score), align="center",
                      font=("courier", 38, "bold"))

        # creating play button

        # play_again = turtle.Turtle()
        # play_again.speed(0)
        # play_again.shape("rectangle")
        # play_again.bgcolor("purple")
        # play_again.goto(0,0)
        # play_again.write("play again \n" , align="bottom" ,font=("courier", 38, "bold") )


        time.sleep(delay)
    # snake collision

    for f in old_food:
        if f.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("purple")
            scoring.goto(0, 0)
            scoring.write(" Game Over!!! \n Your Score is : {} ".format(score), align="center",
                          font=("courier", 38, "bold"))

            # creating play button

            # play_again = turtle.Turtle()
            # play_again.speed(0)
            # play_again.shape("rectangle")
            # play_again.bgcolor('black')
            # play_again.goto(0, 0)
            # play_again.write("play again \n", align="bottom", font=("courier", 38, "bold"))


    time.sleep(delay)
turtle.Terminate()