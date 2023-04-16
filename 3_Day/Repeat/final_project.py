print('Welcome to Treasure island. Your mission is to find the treasure.\n')

first_choice = input('left or right').lower()

if first_choice == 'left':
    second_choice = input('swim or wait')
    if second_choice == 'wait':
        thired_choice = input('Red or Blue or Yellow Door').lower()
        if thired_choice == 'red':
            print('Burned by fire')
        elif thired_choice == 'yellow':
            print('You Win!')
        elif thired_choice == 'blue':
            print('Eaten by beasts. Game Over.!')
        else:
            print('Game Over')
    else:
        print('Attacked by trout Game Over.')
else:
    print('Fall into a hole. Game over')