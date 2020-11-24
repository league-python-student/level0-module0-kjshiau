import turtle


def getNextColor(i):
    return colors[i % len(colors)]

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    Lilly = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    Lilly.shape("turtle")
    # Set your turtle's speed using .speed(2)
    Lilly.speed( 3 )
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Lilly.color("black")
    Lilly.pencolor("black")
    # Move your turtle forward using .forward(100)
    Lilly.forward(100)
    # TEST    Did your turtle move forward?
    # Move your turtle left or right using .left(90) or .right(90)
    Lilly.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.

    for i in range(4):
        Lilly.forward(100)
        Lilly.left(90)
        Lilly.forward(30)
        Lilly.right(180)
    # TEST    Did your turt
    #le draw a square?
    # Move your turtle to a new place on the screen using .goto(x, y)
    Lilly.goto(0, 0)
    # x=0 and y=0 is the center of the screen
    
    # Have your turtle draw a circle using .circle(radius, steps=30)
    Lilly.fillcolor("red")
    Lilly.begin_fill()
    Lilly.circle(radius=100, steps=30)
    Lilly.end_fill()
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle
    Lilly.fillcolor("yellow")
    Lilly.begin_fill()
    Lilly.circle(radius=50, steps=30)
    Lilly.end_fill()

    Lilly.fillcolor("blue")
    Lilly.begin_fill()
    Lilly.circle(radius=25, steps=30)
    Lilly.end_fill()
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    for k in range (4):
        for i in range (14):
            Lilly.fillcolor(getNextColor(i))
            Lilly.begin_fill()
            Lilly.circle(radius=300 - (i*30), steps=30)
            Lilly.end_fill()

        Lilly.right(90)



# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
