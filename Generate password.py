## Easy and simple way to create password

import random

letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['.', ',', ':', ';', "'", '"', '!', '?', '-', '–', '—', '(', ')', '{', '}', '[', ']', '/', '|', '@', '+']
number = ['1','2','3','4','5','6','7','8','9','0']
print("Welcome to password generator program\n"
      "Please Answer about your choice\n")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = ""

# for char in range(1, nr_letter +1):
#       random_char = random.choice(letter)
#       password += random_char
#
#
# for sym in range(1, nr_numbers +1):
#       random_sym = random.choice(symbols)
#       password += random_sym
#
# for num in range(1, nr_numbers + 1):
#       random_num = random.choice(number)
#       password += random_num
#
# print(password)

##Hard and storng password creating

password_list = []

for char in range(1, nr_letter + 1):
      ran_char = random.choice(letter)
      password_list.append(ran_char)

for sym in range(1, nr_symbols +1):
      ran_sym = random.choice(symbols)
      password_list.append(ran_sym)

for num in range(1, nr_numbers +1):
      ran_num = random.choice(number)
      password_list.append(ran_num)

print(password_list)
random.shuffle(password_list)
print(password_list)

## now make list into string

password= ""

for char in password_list:

      password += char

print("Your passwor is :" + password)








