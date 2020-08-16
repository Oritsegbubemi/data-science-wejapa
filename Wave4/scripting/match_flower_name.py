#For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt
flower_dict = {}


# HINT: create a function
def flower(x):
    with open('flowers.txt', 'r') as f:
        myflower = f.readlines()
        for i in myflower:
            i = i.split(': ')
            flower_dict[i[0]] = i[1]
        output = flower_dict[x]
        return output


username = input("Enter your First [space] Last name only: ")
first_letter = username[0].upper()

print(flower(first_letter))
