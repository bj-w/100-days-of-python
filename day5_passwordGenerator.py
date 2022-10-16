from os import sync
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
# get random letters
for letter in range(1, nr_letters + 1):
    password_list += random.choice(letters)
# get random symbols
for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
# get random numbers
for symbol in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
# randomise order of characters
random.shuffle(password_list)
# combine shuffled characters into a string
password = ""
for i in password_list:
    password += i
# output password
print(f"Your password is: {password}")