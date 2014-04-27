''' lesson 2 - building a movie website
build a site that hosts movie trailers and their info

steps:
    1. we need:
        title
        synopsis
        release date
        ratings
    this means we need a template for this data,
        ex: avatar.show_info(), toyStory.show_trailer()
    but we dont want to use separate modules/files for each movie


CLASSES
learning classes by drawing shapes
classes is a lot like a blueprint
    same blueprint can be used to make similar buildings
    objects are examples of the class blueprint

turtle module
Turtle class
    a neatly packaged box
    turtle.Turtle()
        calls the function __init__ w/in class Turtle
        creates a new instance of Turtle and inherits all of the methods

webbrowser.open() vs turtle.Turtle()
    the first calls a function
    the second calls the init func, which allocates memory and creates an obj

steps to make multiple squares that make a circle
    1. build a square
    2. for n < 360/tiltangle, tilt by some amount and build another square

'''
import turtle

def drawThings():
    redbox = turtle.Screen()
    redbox.bgcolor("red")

   # brad = turtle.Turtle()
   # brad.shape("turtle")
   # brad.color("blue")
   # brad.speed(60)
    sunny = turtle.Turtle()
    sunny.shape("turtle")
    sunny.color("black")
    sunny.speed("3")
    
    '''     draws a series of squares that make a circle
    num = 1
    tiltAngle = 6
    tilts = 360 / tiltAngle
    drawSquare(brad)
    while num < tilts:
        brad.right(tiltAngle)
        drawSquare(brad)
        num += 1
    '''
    
    drawSunnysName(sunny)

    redbox.exitonclick()

   # angie = turtle.Turtle()
   # angie.shape("arrow")
   # angie.color("yellow")
   # drawCircle(angie)

def drawSunnysName(person):
    # draws the letter 'S'
    person.left(90)
    person.circle(100, 270)
    person.circle(-100, 270)
    
    # moves the turtle to draw the next letter
    person.penup()
    person.forward(100)
    person.right(90)
    person.forward(600)
    person.pendown()

    # draws the letter 'G'
    person.left(90)
    person.penup()
    person.circle(200, 45)
    person.pendown()
    person.circle(200, 315)
    person.left(90)
    person.forward(200)

def drawSquare(someTurtle):
    for i in range(1, 5):
        someTurtle.forward(100)
        someTurtle.right(90)

def drawCircle(someTurtle):
    someTurtle.circle(100)



main()
