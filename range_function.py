# 18/09/2026
# range function(end)
# list should shows in []
print(list(range(3)))
# 0 1 2
print(list(range(10)))
print(list(range(-5))) #jump 1
print(list(range(0)))
print(list(range(1)))


#range 1 (start,end)
print(list(range(1,3)))
print(list(range(-5, -1)))
print(list(range(-4, -10))) #invalid n+1 formulaa according -4+1 = -3, so this is not valid 
print(list(range(5, 1))) #invalid

# 21/09/2026
# Range variations 2

print(list(range(1,6,2))) #jump 2 means 1 gap and give output 1, 3, 5
print(list(range(0,-5,-1))) #0, -1 , -2, -3, -4
print(list(range(0,-5,1))) #give error  because its forward 
print(list(range(-5,0,-1))) 
print(list(range(0,5,1))) # 0 to 4
print(list(range(-5,-10,-1))) #-5, -6, -7, -8, -9
print(list(range(-4, -6))) # its take by default 1 jump so means its going forward -3 so its give empty string
print(list(range(5))) #0 to 4

#for is itreator
#range is iterable
#  i only variable name , give any name or itreator
for i in range(10):
    print(i)

# print number from 1 to 100
for i in range(1, 101): #because its take from 1 so start and end value print
    print(i)

print(list(range(5))) # 0 to 4
print(list(range(5, 15, 2))) # 5, 7, 9, 11, 13
print(list(range(-5, 0, 1))) #-5, -4, -3, -2, -1
print(list(range(0,1)))

# if any word or sentence you print many times , use for loop
for i in (list(range(0,1))):
    print("Hello")
# 23/09/2026[wednesday] - ma'am absent on his day

# 25/09/2001
# break and continue
# break
for i in range(10):
    if i ==5:
        break # after break no any statemnet prints like after 4 no output print because of break
    print(i)
# Continue
for i in range(10):
    if i == 5:
        continue #5 skip any other output print till 9
    print(i)

# Good programming practice: if you dont use variable in for loop replace it with _
for _ in range(5):
    print("Devanshi") # (5 times devanshi print)variable like if i i am put and its variable not use any where that time i use the _ because its not use

# Pass
   # It is not to be used in compettive programming or interviews, it is usually used in testing, the pass does nothing.
   # It signifies that the programmer will later add some code to it.
   # Right now ignore this block.

for i in range(5):
    if i%2 == 0:
        pass #pass is nothing to give out oyt after pass code still goint next code it for now tester no know about the outpu so they use "Pas statemnet"
    print("Other statemenet")

# Continue
for i in range(0,10):
    if i % 3 == 0: # if staemnet is divided by 3 then that output not print and go to the print statennet
        continue
    print(i, end=" ") #(1 2 4 5 7 8 )use space with all printed numbers thats why use space in end statemnet

# Break
for i in range(1,10):
    if i % 3 == 0:
        break #after break apply then after nothing to print
    print(i, end = " ")
print() #next code excute after this orevious so that's why use this print blank statembet to go new line

# Nested loop
#  * * * 
#  * * * 
#  * * * 
for _ in range(3): # use for raw (also use 2 in this and in column wtite 4 so print 2 row and 4 column)
    for _ in range(3): # use for column
        print("*", end = " ")
    print() #For going to next line print statemnt after finish row
    
