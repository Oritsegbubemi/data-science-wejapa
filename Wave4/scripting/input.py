#Write a script that does the following:

#Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.

#Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.


#Template code for your script:
user_name = []
user_assignments = []
user_grades = []
current_grade = []
i = 0

while (i < 3):
  names =  input("Enter name: ")
  assignments = int(input("Enter the number of assignments: "))

  grades =  int(input("Enter list of grades: ")) 

  current = grades + (2 * assignments)
  
  user_name.append(names)
  user_assignments.append(assignments)
  user_grades.append(grades)
  current_grade.append(current)
  print("")

  i = i + 1


# message string to be used for each student your for loop
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for (name, assignment, grade, current) in zip(user_name, user_assignments, user_grades, current_grade):
  message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
  submit before you can graduate. You're current grade is {} and can increase \
  to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, current)

  print(message)



