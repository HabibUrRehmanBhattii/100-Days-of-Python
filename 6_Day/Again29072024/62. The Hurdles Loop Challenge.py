
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


#for _ in range(6):
#    one_step()

numbers_of_hurdle = 6

while numbers_of_hurdle > 0:
    one_step()
    numbers_of_hurdle -= 1