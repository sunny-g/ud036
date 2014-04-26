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

turtle module
Turtle class
    a neatly packaged box
    turtle.Turtle()
        calls the function __init__ w/in class Turtle
        creates a new instance of Turtle and inherits all of the methods



'''
import turtle

def drawArt():
    redbox = turtle.Screen()
    redbox.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)
    drawSquare(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    drawCircle(angie)

def drawSquare(someTurtle):
    for i in range(1, 5):
        someTurtle.forward(100)
        someTurtle.right(90)

def drawCircle(someTurtle):
    someTurtle.circle(100)



drawArt()
