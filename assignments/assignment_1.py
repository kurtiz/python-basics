""" 
Write a python script that takes input from a user and display it to the
user in a well foramtted output. (use the concept of Lists)
Details:
Name, Age, Class, Gender, Telephone
"""

userDetails = []
userInput = input("Enter a name: ")
userDetails.append(userInput)
userInput = input("Enter age: ")
userDetails.append(userInput)
userInput = input("Enter class: ")
userDetails.append(userInput)
userInput = input("user gender: ")
userDetails.append(userInput)
userInput = input("Enter user telephone: ")
userDetails.append(userInput) 

print(f"Your name is {userDetails[0]}. Your age is {userDetails[1]}. Your class is {userDetails[2]}. Your gender is {userDetails[3]}. Your telephone is {userDetails[4]}")

# print(userInput)
# print(userDetails)
