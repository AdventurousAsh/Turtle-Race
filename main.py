import turtle
import random

#Creates the screen object
screen = turtle.Screen()
screen.setup(600, 300)
screen.title("Turtle Races")

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

turtleDict = {
"red":red,
"orange":orange,
"yellow" : yellow, 
"green" : green, 
"blue" : blue,
"purple" : purple,
}

for key in turtleDict:
    turtleDict[key].shape("turtle")
    turtleDict[key].penup()

playerGuess = turtle.textinput("Turtle Races", "Please input color of turtle you think will win.")

def moveTurtles(turtles):
    #Shuffles the turtles
    x, y = 0, 0
    for key in turtles:
        distance = random.randint(0,10)
        turtles[key].forward(distance)

        x, y = turtles[key].position()
        if x > 270:
            return False
    return True

def checkWinner(turtles):
    x, y = 0, 0
    for key in turtles:
        x, y = turtles[key].position()
        if x > 270:
            return key
    
    return None

while checkWinner(turtleDict) == None:
    moveTurtles(turtleDict)

winner = checkWinner(turtleDict)

if playerGuess.lower() == winner:
    turtle.textinput("Turtle Races", ("You were right! " + winner + " won!!!!"))
else:
    turtle.textinput("Turtle Races", ("You lost. You guessed " + playerGuess + " but " + winner + " won. Press enter to exit."))

#Exits the screen on click
screen.exitonclick()


