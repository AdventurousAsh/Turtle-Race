import turtle
import random

#Creates the screen object
screen = turtle.Screen()
screen.setup(600, 300)

#Creates all of the turtles 
red = turtle.Turtle()
orange = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
purple = turtle.Turtle()

#Adds color and starting position to turtles
red.color("red")
red.teleport(-270, -110)
orange.color("orange")
orange.teleport(-270, -62)
yellow.color("yellow")
yellow.teleport(-270, -14)
green.color("green")
green.teleport(-270, 34)
blue.color("blue")
blue.teleport(-270, 82)
purple.color("purple")
purple.teleport(-270, 130)

turtleList = [red, orange, yellow, green, blue, purple]

for shell in turtleList:
    shell.shape("turtle")


def moveTurtles(turtles):
    #Shuffles the turtles
    x, y = 0, 0
    random.shuffle(turtles)
    for shell in turtles:
        distance = random.randint(0,10)
        shell.forward(distance)

        x, y = shell.position()
        if x > 270:
            return False
    return True

def checkWinner(turtles):
    x, y = 0, 0
    for shell in turtles:
        x, y = shell.position()
        if x > 270:
            return shell
    
    return None

while checkWinner(turtleList) == None:
    moveTurtles(turtleList)





#Exits the screen on click
screen.exitonclick()


