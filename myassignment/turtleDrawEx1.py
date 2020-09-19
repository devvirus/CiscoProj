import turtle


# Screen() method to get screen 
wn = turtle.Screen()

# creating tess object 
geoShape = turtle.Turtle()


def square(x, y):
    # it is used to draw out the pen 
    geoShape.penup()

    # it is used to move curson at x  
    # and y position 
    geoShape.goto(x, y)

    # it is used to draw in the pen 
    geoShape.pendown()
    # turn cursor 45 degree left 
    geoShape.left(45)
    for i in range(4):
        # move cursor 75 unit(pixels)  
        # digit forward 
        geoShape.forward(75)

        # turn cursor 90 degree left 
        geoShape.left(90)

        # Again,move cursor 100 unit  
        # digit forward 
        geoShape.forward(75)


def hexagon(x, y):
    for i in range(6):
        # move cursor 100 unit  
        # digit forward 
        geoShape.forward(100)

        # turn cursor 60 degree left 
        geoShape.left(60)

        # Again,move cursor 100 unit  
        # digit forward 
        geoShape.forward(100)


hexagon(0, 0)
# # it is used to draw out the pen 
turtle.penup()

# turn cursor 45 degree left 
turtle.left(45)
# move cursor 120 unit  
# digit forward 
turtle.forward(120)

# it is used to draw in the pen 
turtle.pendown()
# create circle with radius 120
turtle.circle(120)

# # it is used to draw out the pen 
turtle.penup()

# turn cursor 120 degree left 
turtle.left(120)
# move cursor 50 unit forward 
turtle.forward(50)

# # it is used to draw in the pen 
turtle.pendown()
# draw square with at postion x-55 and y-120
square(55, 120)

# hold the screen  
turtle.done()
