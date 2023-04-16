# List

fruit = ['Apple', 'Banana', 'Orange']
print(fruit[0])
print(fruit[-1])
print(fruit[-2])

fruit[0] = 'Pineapple'
print(fruit)

fruit.append('Grape')
print(fruit)

fruit.insert(1, 'Mango')
print(fruit)

fruit.remove('Grape')
print(fruit)

# pop is a method to delete the last element like pop(0) is to delete the first element of the list
# fruit.pop() will delete the last element of the list
fruit.pop()
print(fruit)

