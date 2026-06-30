# File: ToyCar.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: C S 303E
# 
# Date: 10/15/25
# Description of Program: This program simulates a toy car moving in a 2D grid.

NORTH = 90
EAST = 0
SOUTH = 270
WEST = 180

class ToyCar:

    def __init__( self, x = 0, y = 0, d = EAST ):
        # The initializer for the class (include default values: 0, 0, east); you can assume that the arguments are 
        # integers, but validate that d is a legal value
        if (d != EAST) and (d != NORTH) and (d != WEST) and (d != SOUTH):
            print("ERROR: Illegal direction entered.")
        else:
            self.__direction = d
        self.__x = x
        self.__y = y

    def __str__( self ):
        # String representation of the car information
        return "Your car is at location (" + str(self.__x) + ", " + str(self.__y) + "), heading " + self.__get_direction_str()
    
    def __get_direction_str(self):
        # Return a string representation of the car's direction
        if self.__direction == EAST:
            return "East"
        elif self.__direction == NORTH:
            return "North"
        elif self.__direction == WEST:
            return "West"
        elif self.__direction == SOUTH:
            return "South"

    def setDir( self, d = EAST ):
        # Validate the parameter is legal and set the direction accordingly (default to east)
        if (d != EAST) and (d != NORTH) and (d != WEST) and (d != SOUTH):
            print("ERROR: Illegal direction entered.")
        else:
            self.__direction = d
            print("DEBUG: setting direction " + self.__get_direction_str())

    def getDir( self ):
        # Return the direction (one of 0, 90, 180, 270)
        return self.__direction

    def getX( self ):
        # Return the Y coordinate of the car's location
        return self.__x

    def getY( self ):
        # Return the Y coordinate of the car's location
        return self.__y

    def turnLeft( self ):
        # Change direction 90 degrees to the left
        if self.__direction == NORTH:
            self.__direction = WEST
        elif self.__direction == EAST:
            self.__direction = NORTH
        elif self.__direction == SOUTH:
            self.__direction = EAST
        elif self.__direction == WEST:
            self.__direction = SOUTH
        print("DEBUG: turning " + self.__get_direction_str())

    def turnRight( self ):
        # Change direction 90 degrees to the right
        if self.__direction == NORTH:
            self.__direction = EAST
        elif self.__direction == EAST:
            self.__direction = SOUTH
        elif self.__direction == SOUTH:
            self.__direction = EAST
        elif self.__direction == WEST:
            self.__direction = NORTH
        print("DEBUG: turning " + self.__get_direction_str())

    def forward( self, n ):
        # Validate that n is non-negative and then move the car in the current direction
        if n < 0:
            print("ERROR: Illegal distance entered.")
            return
        print("DEBUG: moving forward " + str(n))
        if self.__direction == NORTH:
            self.__y += n
        elif self.__direction == SOUTH:
            self.__y -= n
        elif self.__direction == EAST:
            self.__x += n
        elif self.__direction == WEST:
            self.__x -= n

def goto( car, x, y ):
    # Moves car to X coordinate
    current_x = car.getX()
    if x > current_x:
        car.setDir(EAST)
        car.forward(x - current_x)
    elif x < current_x:
        car.setDir(WEST)
        car.forward(current_x - x)

    # Moves car to Y coordinate
    current_y = car.getY()
    if y > current_y:
        car.setDir(NORTH)
        car.forward(y - current_y)
    elif y < current_y:
        car.setDir(SOUTH)
        car.forward(current_y - y)

def main():
    c1 = ToyCar( 100, -100, SOUTH )     # Create car c1
    print( c1 )                         # and show its state

    c2 = ToyCar()                       # create car c2
    print( c2 )                         # and show its state

    c3 = ToyCar( y = -50, d = 90 )      # create car c3
    print( c3 )

    c = ToyCar( d = NORTH )             # create car c
    print( c )

    print( c.getDir() )                 # where is c headed?

    c.setDir( 45 )                      # this should fail
    print( c )

    c.forward( 100 )                    # move c forward 100
    print( c )

    c.turnLeft()                        # turn c left
    print( c )

    c.forward( -50 )                    # this should fail

    c.forward( 50 )                     # move c forward 50
    print( c )

    c.setDir( SOUTH )                   # turn c toward the south
    print( c )

    c.turnRight()                       # turn c right (West) 
    print( c )

    c.forward( 25 )                     # move c forward 25
    print( c )

    goto( c, 0, 0 )                     # call your external function 
    print( c )                          # to go to (0, 0)

    goto( c, 100, 100 )                 # now goto (100, 100)
    print( c )

    print( c.getX() )                   # get the current X
    print( c.getY() )                   # get the current Y

main()