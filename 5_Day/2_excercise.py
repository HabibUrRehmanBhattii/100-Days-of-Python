# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Don't use the max() function to do the max of the numbers in a list and min() function. You should use a for loop and an if statement.

# 1. Create a variable called highest_score and set it to 0.
# 2. For each score in the student_scores list:
# 3. If the score is higher than the current highest_score, then set the highest_score to the score.
# 4. Print the highest score.


heighest_score =0
for score in student_scores:
    if score > heighest_score:
        heighest_score = score

print(f"The heighest score in the class is: {heighest_score}")


# for lowest_score in student_scores:

lowest_score = 100
for score in student_scores:
    if score < lowest_score:
        lowest_score = score

print(f"The heighest score in the class is: {lowest_score}")



