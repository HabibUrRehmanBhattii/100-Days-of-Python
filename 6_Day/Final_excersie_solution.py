def turn_right():
    turn_left()
    turn_left()
    turn_left()

# For debugging purposes, where robot has to rigt waal

while front_is_clear():
    move()
turn_left()

# the move() function will move the robot forward until it hits a wall
# the turn_left() function will turn the robot left to right of the wall
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
