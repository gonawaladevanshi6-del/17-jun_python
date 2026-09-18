# input function
# input()is used in python for taking user from input.
# we can also pass the mesasage in input()
# which will be printed for taking input from user 
# input() will always return a string value.

# a=input()
# print(type(a))
# print(a)

a=input("Enter your name: ")
print(type(a))
print(a)
# convert type when user give value
age=int(input('Enter your age: '))
print(type(age))
print(age)

# sep and end
# we can pass the sep and end values in the print statement.
# sep is what should come between the values of the print statemnet.
# end: is what should come after the print statement.
# content default value of sep is ' ' (space) and end is \n(new line character)

print(12,1234,123,789)
print("hello")

print('John', 'doe',sep='-')
a=10
b=20
c=30
print(a,b,end =' ') #10 20
print(c)#30
print(1,2,3,4,sep="-",end="+")
print(5)


