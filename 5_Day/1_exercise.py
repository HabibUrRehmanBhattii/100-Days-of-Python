# 🚨 Don't change the code below 👇


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height += height

#  total height = (student_heights)
total_students = 0
for students in student_heights:
    total_students += 1

average_height = round(total_height/total_students)

print(average_height)


#Write your code above this row 👆

# Don't use the sum() function to do the sum of the numbers in a list. You should use a for loop. and the len() function to get the length of the list.
# 1. Create a list of student heights.
# 2. Write a for loop to calculate the sum of all the heights in the list.
# 3. Write a for loop to calculate the total number of students in the list.
# 5. Calculate the average height using the sum of heights and the total number of students.
# 6. Print the average height rounded to the nearest whole number.