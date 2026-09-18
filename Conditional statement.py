# Conditional statement

# m_comp = 120
# m_culture = 'positive'
# m_distance = 300

# g_comp = 110
# m_culture = 'positive'
# m_distance = 30

# if m_comp>80:
#     print("Microsoft Criteria filled!!!")
# elif g_comp>80:
#     print("Google Criteria Filled!!!")
# else:
#     print("sad life!!!")

# Nested
m_comp = 110
m_culture = 'positive'
m_distance = 300

g_comp = 110
g_culture = 'Positive'
g_distance = 3000

if m_comp>80 and g_comp>80:
  if m_distance>g_distance: #[if any both conditiuon should be take true so this if condition write multiple times]
   print('Go to Google')
  else:
   print('Go to Microsoft')

# Problem Statement : Traffic Lights
# You have to ask about the color of the traffic light from user , if:
# It is green, then print go,
# it is yellow, then print wait,
# It is red, then print stop
# green -> go
# yellow -> wait 
# red -> stop

light=input("Enter the name of light : ")
if light =='green':
   print("go")
elif light == 'yellow':
   print("wait")
elif light == 'red' : #if i enter the color of light is Red = prints invalid input because its cassensitive
   print("stop")
else:
  print("Invalid input...")

