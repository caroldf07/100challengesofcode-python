# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
number_letters = int(
    input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_easy = ""

while number_letters > 0:
    password_easy += random.choice(letters)
    number_letters -= 1
while number_symbols > 0:
    password_easy += random.choice(symbols)
    number_symbols -= 1
while number_numbers > 0:
    password_easy += random.choice(numbers)
    number_numbers -= 1

# print(f"Your medium password is: {password_easy}")
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = ''.join(random.sample(password_easy, len(password_easy)))
print(f"Your strongest password is: {password_hard}")
