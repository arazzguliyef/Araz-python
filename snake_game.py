#imprth some module:
import os
import turtle
import time
import random

#score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("WELLCOME SNAKE GAME OF ARAZ")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  HighScore: 0", align="center", font=("Courier", 24, "normal"))

#Functions:
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
       x = head.xcor()
       head.setx(x + 20)

#keyboard adding:
wn.listen()
wn.onkeypress(go_up, "5")
wn.onkeypress(go_down, "2")
wn.onkeypress(go_left, "1")
wn.onkeypress(go_right, "3")

#main game loop:
while True:
    wn.update()
    
    if head.xcor()> 290 or head.xcor()< -290 or head.ycor()> 290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segments in segments:
            segments.goto(1000, 1000)

        segments = []

        score = 0

        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        #increasing score:
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) -1, 0 , -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor() 
            segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y) 

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segments in segments:
                segments.goto(1000, 1000)

            segments = []
  
            score = 0

            pen.clear()
            pen.write("Score: {} HighScore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
  
    time.sleep(0.1)


wn.mainloop()

# python language()
