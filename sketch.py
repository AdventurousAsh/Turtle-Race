import turtle

#Creates the "turtle" object
bob = turtle.Turtle()

#Creates the screen object
screen = turtle.Screen()

distance = 4

def moveForward():
    bob.forward(distance)

def moveBack():
    bob.backward(distance)

def counterClock():
    bob.left(5.0)

def clockwise():
    bob.right(5.0)

def clearAndReset():
    bob.clear()
    bob.teleport(0,0)

#Creates listener for events
screen.listen()
#Lists the event that we are listening for and what to do with them
screen.onkeypress(key="w", fun= moveForward)
screen.onkeypress(key="s", fun= moveBack)
screen.onkeypress(key="a", fun= counterClock)
screen.onkeypress(key="d", fun= clockwise)
screen.onkeypress(key = "c", fun= clearAndReset)

#Exits the screen on click
screen.exitonclick()