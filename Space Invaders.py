#Space Invaders:
import turtle
import os
import math
import random

#set up the screen:
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#wn.bgpic("2.gif")

#register the shape:
#enemy.register_shape("araz.gif")
#player.register_shape("3.jpg")

#darw border:
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()    

#set e score to 0:
score = 0

#draw score:
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition (-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player turtle:
player = turtle.Turtle()
player.color("blue")
player.shape("circle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#choose a number of enemies:
number_of_enemies = 10

#create empty list:
enemies = []

#add enemies to list
for i in range(number_of_enemies):
    #Creating Enemmy:
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("square")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 250)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 3

#creat the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state:
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move player right and left:
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)  

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move wallet:
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y) 
        bullet.showturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#creating keyboard binging:
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# main game loop:
while True:
    #wn.update()
    
    for enemy in enemies:  
        #move the enemy:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 290:
            #move all enemies:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -290:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            #reset bullet:
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            #reset the enemy:
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            
            #Update the score:
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    #move bullet:
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
