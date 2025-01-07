letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
symbols = ['.', ',', ':', ';', "'", '"', '!', '?', '-', '–', '—', '(', ')', '{', '}', '[', ']', '/', '|', '@', '+']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print("Welcome to password generator program\n"
          "Please Answer about your choice\n")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


def create_password():
    # password generator

    # first easy part
    import random
    from random import shuffle



    self_password = ""

    for let in range(1, nr_letter + 1):
        random_char = random.choice(letter)
        self_password += random_char

    for num in range(1, nr_numbers + 1):
        random_num = random.choice(number)
        self_password += random_num
    for sym in range(1, nr_symbols + 1):
        random_sym = random.choice(number)
        self_password += random_sym

    print(self_password)

    ###Hard part and create strong password

    self_password_list = []
    for let in range(1, nr_letter + 1):
        self_password_list.append(random.choice(letter))
    for sym in range(1, nr_symbols):
        self_password_list.append(random.choice(symbols))
    for num in range(1, nr_numbers + 1):
        self_password_list.append(random.choice(number))

    shuffle(self_password_list)

    self_password_list_main = ""
    for char in self_password_list:
        self_password_list_main += char
    print("Your password is : " + self_password_list_main)

for step in range(100000):
    create_password()
