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

