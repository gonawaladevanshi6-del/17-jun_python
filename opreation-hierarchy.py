# 15/09/2026
# () - parentheses
# ** - power
# *,/,//,% - multiply, divide, floor division, modules - left to right
# +,- => addition, substraction
# !=, == not equal, equal
# <,<=,>,>= -> comparission opreator
# not -> NOT
# and -> AND
# or -> OR
print(3*10 /2)
print((3*10) /2) #15 hi aayega per ()-parentheses pehele excute hoga  as per rule
print(45 % 10 /2) #left to right pehle mod hoga fir divide
print(True and not False)

# Scopping [inditation]
a = 5
if a>10:    
    print(a)        
    if a%5==2:  
      print("Bla")
else:
   print(a)
   print('1234') # this is output because in first if a[5] is not grater than 10 and if 1st condition wrong so statement not check the if 2nd conditionso run else 

# ittratiion while condition
print("Five")
print("Five")
print("Five")
'''
variable initialization
while (condition)
{
action
update variable
}
'''
# while
# print numbers from 1 to 15
# count = 1 # starting valsue of variable value (give any variable name) 
# while(count<=15):
#    print(count)
#    count+=1 

# break
# count = 1
# while(count<=15):
#    if count == 10:
#       break
#    print(count)
#    count+=1

# continue [continue statemnet me count jo variable hote hai vo first aa jayega]
# count = 0
# while(count<=15):
#    count+=1
#    if count ==10:
#       continue
#    print(count)

# count = 0
# while count <= 5: #5<=5
#    count +=1
#    if count == 3: #6==3
#       continue
#    print(count) #5

# While else [if break statement write - after the break else statemnet also not run]
count = 0 #initialization
while count<=15: #condition
   count+=1 #1
   print(count) #1
   if count == 10: 
      break
else:
    print("Completed")
    print("Yay")

      
