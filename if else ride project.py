#if else (ride validation check program
height = float(input("Enter your height in cm : "))
bill = 0
if height>=120:
    print(f'Your height is {height}\n'
          f'Go to next question')
    age = int(input("What is you age : "))

    if age <=12 :
        bill=5
        print(f'Your age is {age}.For ride you have to pay only ${bill}')
        answer = input("Do you want to ride by paying $5 (yes/no)")
        if answer == "yes" or answer=="y":
            print("Congratulation, go to enjoy your ride")


        else:
            print("Go to Hell")
    elif age <= 18:
        bill=10
        print(f"You are {age} year old. For ride you have to pay ${bill} ")
        answer1 = input("Do you want to ride by paying $10 (yes/no )")
        if answer1 == "yes" or answer1=="y":
            print("Congratulation, go to enjoy your ride")
        else:
            print("Go to Hell")

    elif 45 <= age <= 55:
        bill = 0
        print(f"You are {age} year old. Congratulation you can ride free pay ${bill} ")


    else:
        bill = 18
        print(f"You are {age} year old. For riding you have to pay ${bill}")
        print()
        answer2 = input("Do you want to ride by paying $10 (yes/no )")
        if answer2 == "yes" or answer2=="y":
            print("Congratulation, go to enjoy your ride")
        else:
            print("Go to Hell")

    click_photo = input("Do you want to take photo during ride (yes/no)")
    if click_photo == "yes":
        print("For click photo you have to pay extra $3 ")
        conform_add_money = input("Do you want to spend money for photo (yes / no) ")
        if conform_add_money=="no":
            print(f'Your total bill is : ${bill}')
        else :
            bill += 3
            print(f"Your total bill is : ${bill}")


    else:
        print(f"Your total bill is ${bill}")



else:
    print(f"Your height is {height}\n"
          "For ride Minimum height is 120\n"
          "Sorry...Your are not ready for ride")