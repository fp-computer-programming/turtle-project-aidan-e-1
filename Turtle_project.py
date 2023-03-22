#author ate (3/6/23)

#needed import
import random
import turtle

#variables
window = turtle.Screen()
window.title("Tic-Tac-Toe game")
window.bgcolor("crimson")
billy = turtle.Turtle()
billy.hideturtle()
billy.setx(-125)
billy.sety(0)
billy.speed(3)
billy.color("yellow")
billy.shape("turtle")

#main body of code
#code for drawing graph
billy.stamp()
billy.forward(200)
billy.stamp()
billy.back(65)
billy.left(90)
billy.forward(120)
billy.back(180)
billy.stamp()
billy.penup()
billy.forward(120)
billy.stamp()
billy.right(90)
billy.pendown()
billy.forward(65)
billy.stamp()
billy.back(200)
billy.stamp()
billy.penup()
billy.forward(50)
billy.left(90)
billy.pendown()
billy.forward(59)
billy.stamp()
billy.back(180)
billy.stamp()

#code for drawing AI and player chose of spots
steve = turtle.Turtle()
steve.color("purple")
steve.pensize(4)
steve.shape("square")
steve.hideturtle()
fred = turtle.Turtle()
fred.color("white")
fred.pensize(4)
fred.shape("circle")
fred.hideturtle()

#AI 1
steve.penup()
steve.setx(45)
steve.sety(90)
steve.pendown()
steve.stamp()

#player 2
fred.penup()
fred.setx(-105)
fred.sety(-35)
fred.pendown()
fred.stamp()

#AI3
steve.penup
steve.goto(-45, 90)
steve.pendown()
steve.stamp()

#player 4
fred.penup
fred.goto(0, -35)
fred.pendown()
fred.stamp()

#AI 5
steve.penup
steve.goto(45, -90)
steve.pendown()
steve.stamp()

#player 6
fred.penup
fred.goto(5, 90)
fred.pendown()
fred.stamp()

#AI 8
steve.penup
steve.goto(0, 90)
steve.pendown()
steve.stamp()

#player 9
fred.penup
fred.goto(0, 0)
fred.pendown()
fred.stamp()

#window perma-open
window.mainloop()