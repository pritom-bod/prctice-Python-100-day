print(len("hello"))
##datatyps
print("hello"[-4])
print("123"+ "ojih")
#integer
print(12332+94395-54385)
#large integer
print(23423_8343_3247)
#float
print(3.55556)
#Booean
print(True)
print(False)

#data Type
print(type([2,3,5,6]))
# type changing
print(int("347392")-2349)



print("Number of letter in your name : ",int() +
      len(input("Enter Your name : ")))

name = input("Type your name : ")
length = len(name)
print("Total digit of your number is :", length)
## BMI calculation
weight = float(input("Enter your weight : "))
height = (input("Enter your height : " ))
result = (weight/(float(height)**2))
print(round(result, 3))

#make resturdent bill calculator
print("Welcome to the tip calculator")
t_bill = float(input("What was the total bill? :$"))
tip_add = float(input("How much tip would you like to give? "))
main_bill = t_bill+(t_bill*(tip_add/100))
print(f'With adding tip, Your total bill was : {main_bill}')
split = int(input("How many people to split the bill? Answer:"))
Each_parson_bill = main_bill / split
print(f'Each parson should pay : ${round(Each_parson_bill, 2)}')







