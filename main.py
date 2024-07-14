import turtle

#Creates the "turtle" object
bob = turtle.Turtle()

#Creates the screen object
screen = turtle.Screen()

def moveForward():
    bob.forward(5)

#Creates listener for events
screen.listen()
#Lists the event that we are listening for and what to do with them
screen.onkey(key="space", fun= moveForward)
#Exits the screen on click
screen.exitonclick()


