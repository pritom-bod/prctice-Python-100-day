## loop learning

##first for loop
fruits = ["Apple", "Peach", "Pear"]
for i in fruits:
    print(i)
###
student_Scores = [344,454,345,455,453,333,233,454,344,342,234]

total_scores =sum(student_Scores)
print(total_scores)
## done this by using for loop
total_scores = 0
for i in student_Scores:
    total_scores += i
print(total_scores)
##max
max_num =  max(student_Scores)
print(max_num)

##min
min_num = min(student_Scores)
print(min_num)

## find max number by using for loop
max_score = 0
for i in student_Scores:
    if max_score < i:
        max_score = i
print(max_score)
#find min number by using for loop

min_score = 2322332432424324
for i in student_Scores:
    if min_score > i:
        min_score = i
print(min_score)

###add 1 to 100 number using for loop and Renge
total = 0
for i in range(1,101):
    total += i
    print(total)
##
for i in range(1,14,2):
    print(i)












