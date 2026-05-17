
#11. Check gym membership category
'''
age=int(input('Enter your age:'))
weight=int(input('Enter the weight:'))
height=float(input('Enter the height:'))
if age>18 and weight>50 and height>5.5:
    print("Fitness Category A")
elif age>10 and weight>10 and height>2.5:
    print("Fitness Category B")
else:
    print("Basic Category")
''' 
#12. Check traffic penalty system

helmet = input('Do you have helmet: ')
license= input('Do you have license: ')
speed = int(input('Enter speed: '))

if helmet == "yes"and license == "yes" and speed < 80:
    print("No Fine")

elif helmet == "no"and license == "no" and speed < 100:
    print("Heavy Fine")

else:
    print("Normal Fine")