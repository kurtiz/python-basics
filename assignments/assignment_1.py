<<<<<<< HEAD
""" 
Write a python script, declare 4 variables. 
1. two string variables that will take store name and store contact
2. two lists that will take products and their prices respectfully
print them out
"""

# string variables
storeName = "Mega Store"
storeContact = "0567316733"

# list variables
products = ["belt", "amane", "gari", "dawadawa", "beans"]
price = [78.00, 10.00, 35.00, 5.00, 9.00]


print(f"Store Name: {storeName}")
print(f"Store Contact: {storeContact}")
print("========Products=========")
print(products[0],price[0])
print(products[1],price[1])
print(products[2],price[2])
print(products[3],price[3])
print(products[4],price[4])
=======
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
>>>>>>> 733973d51954203c5431bdf0a72e18f0270579c0
