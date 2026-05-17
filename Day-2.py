
 #Question 31
 
 # 31. check employee promotion promotion eligibility
'''
age=int(input('Enter a age:'))
experience=int(input('Enter an experience:'))
salary=int(input('Enter a salary:'))
if(age>25 and experience>5 and salary>50000 ):
    print("Eligible for promotion")
else:
    print("Not eligible")
'''
#Question 32

#32. check student distinction category
'''
maths=int(input('Enter a  marks:'))
scienc=int(input('Enter a  marks:'))
english=int(input('Enter a  marks:'))
if(science>=75 and maths>=75 and english):
 ''' 
'''   
#Question 33 
name=input('Enter a  userName:')
password=int(input('Enter a  password:'))
otp=int(input('Enter a  otp:'))
if(name=='satya' and password=='123' and otp=='123'):
   print("login succesfull")
else:
    print("invalid")
'''

# Question 34
'''
name = input('Enter username: ')
password = input('Enter password: ')
otp = input('Enter otp: ')

if name == 'satya' and password == '123' and otp == '123':
    print("login successful")

elif name == 'vineela' and password == '456' and otp == '456':
    print("login successful")

else:
    print("invalid")
'''  
# Using List
'''
users = ['satya', 'vineela']
passwords = ['123', '456']
otps = ['123', '456']
name = input('Enter username: ')
password = input('Enter password: ')
otp = input('Enter otp: ')
if name == users[0] and password == passwords[0] and otp == otps[0]:
    print("login successful")
elif name == users[1] and password == passwords[1] and otp == otps[1]:
    print("login successful")
else:
    print("invalid")
'''
# Question 35
'''
speed=int(input('Enter a speed:'))
dataUsage=int(input('Enter a data used:'))
remainingDays=int(input('Enter a  days:'))
if(speed>100 and data>500 and days>20):
   print("premium plan")
elif speed>50 and data>200:
    print("standard plan")
else:
    print("Basic plan")
'''
'''
rooms=int(input('Enter rooms:'))
days=int(input('Enter days:'))
budget=int(input('Enter budget:'))
if(rooms>=2 and days>=3 and budget>50000):
   print("luxury booking")
elif speed>50 and data>200:
    print("standard bbooking")
else:
    print("Budget booking")
'''
#15. Check online shopping offer
'''   
purchaseAmount=int(input('Enter purchase amount:'))
couponAvailability=input('Enter couponAvailability:')
premiumMembership=input('Enter budget:')
if(amount > 10000 and coupon == "yes" and member == "yes"):
   print("Maximum Discount")
elif amount>500 and coupon=='yes':
    print("Medium Discount")
else:
    print("No Discount")
'''   

for x in range(10):
    if x%2==0:
        print( x**2)
 #list comprehension       
result=[x**2 for i in range(10) if x%2==0]
print(result)
