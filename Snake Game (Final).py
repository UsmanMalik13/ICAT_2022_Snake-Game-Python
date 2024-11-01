#Importing Libraries
from tabnanny import check
import turtle
import random
import time

def game_function():
        #Creating Screen
        screen = turtle.Screen()
        screen.title("Snake Game")
        screen.setup(width = 700, height = 700)
        screen.tracer(0)
        turtle.bgcolor("black")


        #Creating a Border
        turtle.speed(5)
        turtle.pensize(4)
        turtle.penup()
        turtle.goto(-310,250)
        turtle.pendown()
        turtle.color("green")
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(500)
        turtle.penup()
        turtle.hideturtle()


        #Score Board
        score = 0
        delay = 0.1


        #Snake Head
        snake = turtle.Turtle()
        snake.speed(0)
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(0,0)
        snake.direction = "stop"


        #Food
        fruit = turtle.Turtle()
        fruit.speed(0)
        fruit.shape("circle")
        fruit.color("red")
        fruit.penup()
        fruit.goto(30,30)

        old_fruit=[]

        #Scoring Incrementation and High Score
        scoring = turtle.Turtle()
        scoring.speed(0)
        scoring.color("white")
        scoring.penup()
        scoring.hideturtle()
        scoring.goto(0,300)
        scoring.write("Score :", align = "center", font=("Courier", 24, "bold"))

        #Startup Screen
        startup = turtle.Turtle()
        startup.speed(0)
        startup.color("white")
        startup.penup()
        startup.hideturtle()
        startup.goto(0, 100)
        startup.write("Press Arrow keys to begin", align="center", font=("Courier", 24, "bold"))
        time.sleep(2.5)
        startup.clear()

        #Snake Movement
        def snake_move_up():
                if snake.direction != "down":
                        snake.direction = "up"

        def snake_move_down():
                if snake.direction != "up":
                        snake.direction = "down"

        def snake_move_left():
                if snake.direction != "right":
                        snake.direction = "left"

        def snake_move_right():
                if snake.direction != "left":
                        snake.direction = "right"

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


        #Keyboard Bindings
        screen.listen()
        screen.onkeypress(snake_move_up, "Up")
        screen.onkeypress(snake_move_down, "Down")
        screen.onkeypress(snake_move_left, "Left")
        screen.onkeypress(snake_move_right, "Right")

        #Main Loop
        check = True
        while check == True:
                screen.update()

                #Snake and Fruit Collision
                if snake.distance(fruit) < 20:
                        x = random.randint(-290, 270)
                        y = random.randint(-240, 240)
                        fruit.goto(x,y)
                        scoring.clear()
                        score += 1
                        scoring.write("Score:{}".format(score), align = "center",font=("Courier", 24, "bold"))
                        delay -= 0.001
                        
                        #Creating New Snake Body Part
                        new_fruit = turtle.Turtle()
                        new_fruit.speed(0)
                        new_fruit.shape("square")
                        new_fruit.color("blue")
                        new_fruit.penup()
                        old_fruit.append(new_fruit)
                        
                #Adding Ball to Snake
                for index in range(len(old_fruit) -1, 0, -1):
                        a = old_fruit[index - 1].xcor()
                        b = old_fruit[index - 1].ycor()

                        old_fruit[index].goto(a,b)
                                        
                if len(old_fruit) > 0:
                        a = snake.xcor()
                        b = snake.ycor()
                        old_fruit[0].goto(a, b)
                snake_move()

                #Snake and Border Collision    
                if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('black')
                        scoring.goto(0,0)
                        scoring.write("Game Over\nYour Score was {}".format(score), align="center",font=("Courier", 30, "bold"))
                        restart = screen.textinput("Retry", "Do you want to restart ? (y/n)")
                        if restart == "y" or restart == "Y":
                                screen.clearscreen()
                                game_function()
                        else:
                                check = False
                        
                #Snake and Snake Collision
                for food in old_fruit:
                        if food.distance(snake) < 20:
                                time.sleep(1)
                                screen.clear()
                                screen.bgcolor('black')
                                scoring.goto(0,0)
                                scoring.write("Game Over\nYour Score was {}".format(score), align="center", font=("Courier", 30, "bold"))
                                restart = screen.textinput("Retry", "Do you want to restart ? (y/n)")
                                if restart == "y" or restart == "Y":
                                        screen.clearscreen()
                                        game_function()
                                else:
                                        check = False

                time.sleep(delay)

        turtle.bye()
game_function()
