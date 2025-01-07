# def greet():
#     print("Hello sunny ")
#     print("Hello Tanvir")
#     print("Hello Sourov")
#
# greet()
#create function by using perameter

def greet_with_input(name, age):
    print(f'ki obosthA {name} tomar boyos {age}')
    print(f"kemon aso {name} jonmo sectificate koto {age} ee ase")
    print(f'{name} akhono tui sai boka chodai aso {age} dey naki')

greet_with_input(input("type you name : "), input("type your age : "))
greet_with_input("sani", 25)

##funtion with mor than 1 input

def check_order(name, age, location, father_name, mother_name):
    print(f' I am {name} and I am {age} year old.')
    print(f'my father name is {father_name}, and my mother name is {mother_name}')
    print(f'I live in {location}')
check_order(location=input('Where are you live in : '), mother_name=input('What is you mother name : '), father_name=input('What is your father name : '), name=input('What is your name : f'), age=input('What is you age : '))
