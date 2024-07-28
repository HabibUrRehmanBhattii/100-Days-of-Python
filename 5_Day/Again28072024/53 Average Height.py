student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height
    number_of_students += 1

average_height = total_height / number_of_students
print(total_height)
print(number_of_students)
print(average_height)
