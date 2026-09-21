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
print(list(range(-5, 0, 1))) #[-5, -4, -3, -2, -1
print(list(range(0,1)))

# if any word or sentence you print many times , use for loop
for i in (list(range(0,1))):
    print("Hello")

