# List

fruit = ['Apple', 'Banana', 'Orange']
print(fruit[0])
print(fruit[-1])
print(fruit[-2])

fruit[0] = 'Pineapple'
print(fruit)

# append is a method to add the element to the end of the list
fruit.append('Grape')
print(fruit)

# insert is a method to add the element to the specific index of the list
fruit.insert(1, 'Mango')
print(fruit)

# remove is a method to delete the element from the list
fruit.remove('Grape')
print(fruit)

# pop is a method to delete the last element like pop(0) is to delete the first element of the list
# fruit.pop() will delete the last element of the list
fruit.pop()
print(fruit)

# extend is a method to add the element to the end of the list
fruit.extend(['Grape', 'Watermelon'])
print(fruit)

# count is a method to count the element in the list
print(len(fruit))

# user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')
#
# choice = [rock, paper, scissors]
#
# user_choose = choice[int(user_choice)]
#
# computer_choice = r.randint(0, 2)
# print(computer_choice)
# computer_choose = choice[int(computer_choice)]
#
# if user_choice == computer_choice:
#     print(f'User choose {user_choose}\n Computer choose {computer_choose}\n So it´s a DRAW!')
# elif user_choice == 1 and computer_choice == 3:
#     print(f'User choose {user_choose}\n Computer choose {computer_choose}\n You won! Rock smashes Scissors')
# elif user_choice == 2 and computer_choice == 1:
#     print(f'User choose {user_choose}\n Computer choose {computer_choose}\n You won! Paper covers Rock')
# elif user_choice == 3 and computer_choice == 2:
#     print(f'User choose {user_choose}\n Computer choose {computer_choose}\n You won! Scissors cuts Paper')
# else:
#     print(f'User choose {user_choose}\n Computer choose {computer_choose}\n Computer Won!')