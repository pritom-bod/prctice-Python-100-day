#################################################################################
#############################Today's topic#######################################
##################""Randomisation And Python List""##############################
#################################################################################

#random number
import random
import my_modual
random_number = random.randint(0, 43)
print(random_number)

print(my_modual.my_create_module)
##random floating 0 to 1 number
random_number_0_to_1 = random.random() -3
print(random_number_0_to_1)#
##random floating number
random_floating_number = random.uniform(1,7)
print(random_floating_number)

#head and tail game by using random module
random_head_or_tail= random.randint(0,1)
if random_head_or_tail == 0:
    print("Heads")
else:
    print("Tails")

#Python List important topic
list_of_friends = ['pritom','sany','surov','rajib','tanvir']
print(list_of_friends[4])
#change 1 items from the list

list_of_friends[1] = "sunny"
print(list_of_friends)
#add an item in the list
list_of_friends.append("raju")
print(list_of_friends)

##for add another list with main list

list_of_friends.extend(['ridoy','munna','younus'])
print(list_of_friends)

##Who will pay the bill
list_res_friends = ['pritom', 'sunny', 'sourov', 'rajib', 'tanvir', 'younus']
ran_num=random.randint(0,5)
if ran_num ==0 :
    print(list_res_friends[0])
elif ran_num==1:
    print(list_res_friends[1])
elif ran_num == 2:
    print(list_res_friends[2])
elif ran_num==3:
    print(list_res_friends[3])
elif ran_num==4:
    print(list_res_friends[4])
elif ran_num==5:
    print(list_res_friends[5])


## simple way to random module by choice usig list

print(random.choice(list_res_friends))
##trick using randint

friend_resturadent = ['pritom', 'sunny', 'surov', 'rajib', 'tanvir', 'raju', 'ridoy', 'munna', 'younus']

result = random.randint(0,8)
print(friend_resturadent[result])

print(len(friend_resturadent))

##nested list
added= [friend_resturadent,list_of_friends]
print(added)

















