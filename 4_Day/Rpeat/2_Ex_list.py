import random as r

name_string = input('Give me everybody\'s names, separated by a comma. ')
names = name_string.split(', ')
#  Split the string into a list of names

max_names = len(names)
#  Find the total number of names in the list
random_selection = r.randint(0, max_names - 1)
print(random_selection)

select_person = names[random_selection]

#  Select a random person from the list of names
print(f'{select_person} is going to buy the meal today!')

#
# name_list = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
#
# random_selection = r.randint(0, 4)
#
# selected_person = name_list[random_selection]
#
# print(f'{selected_person} is going to buy the meal today!')
