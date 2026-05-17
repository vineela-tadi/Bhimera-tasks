# Question 1
# 1. Check whether employee age is above 21 and salary is above 30000
'''
age=int(input('Enter your age:'))
salary=int(input('Enter the salary:'))
if age>21 and salary>30000:
    print(True)
else:
    print(False)
  '''  

# Question 2
# 2. Check whether student passed in two subjects
'''
s1=int(input('Enter the marks:'))
s2=int(input('Enter another marks:'))
if s1>=35 and s2>=35:
    print(True)
else:
    print(False)
'''

# Question 3
# 3. Check whether entered value is between two ranges
'''
n=int(input('Enter a number:'))
if n>10 and n<50:
    print(True)
else:
    print(False)
'''

# Question 4
# 4. Check whether username and password are correct
'''
userName = 'vineela'
passWord = 1234
n1 = input('Enter username: ')
n2 = int(input('Enter password: '))
if n1 == userName and n2 == passWord:
    print(True)
else:
    print(False)
'''

# Question 5
# 5. Check whether temperature is within safe range
'''
temp=int(input('Enter temperature:'))
if temp>10 and temp<50:
    print(True)
else:
    print(False)
'''

# Question 6
# 6. Check whether both entered numbers are even
'''
num1=int(input('Enter a number1:'))
num2=int(input('Enter a number2:'))
if num1%2==0 and num2%2 ==0:
    print(True)
else:
    print(False)
'''

# Question 7
# 7. Check whether both entered numbers are positive
'''
num1=int(input('Enter a number1:'))
num2=int(input('Enter a number2:'))
if num1>0 and num2>0:
    print(True)
else:
    print(False)
'''

# Question 8
# 8. Check whether person is eligible for driving
'''
age=int(input('Enter a age:'))
license=(input('Enter a license available or not:'))
if age>=18 and license=='yes':
    print(True)
else:
    print(False)
'''

# Question 9
# 9. Check whether project progress meets deadline condition
'''
days = int(input('Enter remaining days: '))
progress = int(input('Enter progress percentage: '))

if days > 5 and progress >= 80:
    print(True)
else:
    print(False)
'''

# Question 10
# 10. Check whether attendance and marks satisfy eligibility
'''
attendance= int(input('Enter attendance: '))
marks = int(input('Enter marks: '))
if attendance >=75 and marks >= 35:
    print(True)
else:
    print(False)
'''

# Question 11
# 11. Check whether entered role is Admin or Manager
'''
role= input('Enter a value: ')
if  role=='admin' or role=='manager':
    print(True)
else:
    print(False)
'''

# Question 12
# 12. Check whether student scored distinction in any one subject
'''
marks= int(input('Enter a value1:'))
marks1=int(input('Enter a value2:'))
if marks >75 or marks1>75:
    print(True)
else:
    print(False)
'''

# Question 13
# 13. Check whether entered day is weekend
'''
day= input('Enter a day:')
if day=='saturday' or day=='sunday':
    print("weekend")
else:
    print("Not weekend")
'''

# Question 14
# 14. Check whether selected category matches two possible values
'''
category = input('Enter category: ')
if category == 'electronics' or category == 'clothing':
    print(True)
else:
    print(False)
'''

# Question 15
# 15. Check whether salary or experience satisfies requirement
'''
salary = int(input('Enter salary: '))
experience = int(input('Enter experience: '))
if salary > 30000 or experience >= 2:
    print(True)
else:
    print(False)
'''

# Question 16
# 16. Check whether temperature is extremely low or high
'''
temp = int(input('Enter temperature: '))
if  temp<10  or temp> 20:
    print(True)
else:
    print(False)
'''

 # Question 17
# 17. Check whether entered username matches predefined values
'''
userName='vineela'
userName2='satya'
n = input('Enter username: ')
if n==userName  or n==userName2:
   print(True)
else:
   print(False)
'''

 # Question 18
 # 18. Check whether selected option belongs to given choices
'''
n=input('Enter an choice:')
if n=='A' or n=='B'or n=='C':\
     print(True)
else:
    print(False)
'''

 # Question 19
 #19. Check whether entered city matches allowed cities
'''
str1='eluru'
str2='bhimadole'
n=input('Enter an choice:')
if n==str1 or n==str2:
     print(True)
else:
    print(False)
''' 

# Question 20
# 20. Check whether entered number matches predefined values
'''
num = int(input('Enter a number: '))
if num == 1 or num == 2 or num == 3:
    print(True)
else:
    print(False)
'''

# Question 21
# 21. Check whether user is not admin
'''
user = input('Enter username: ')
if user != 'admin':
    print(True)
else:
    print(False)
'''

# Question 22
# 22. Check whether entered number is not positive
'''
num = int(input('Enter number: '))
if not(num >0):
    print(True)
else:
    print(False)
'''

# Question 23
# 23. Check whether entered value is not empty
'''
value= input('Enter a value: ')
if not(value==""):
    print(True)
else:
    print(False)
'''

# Question 24
# 24. Check whether file is not available
'''
fileAvailable=False
if not(fileAvailable):
    print(True)
else:
    print(False)
'''

# Question 25
# 25. Check whether employee is not active
'''
active=False
if not(active):
    print(True)
else:
    print(False)
'''

# Question 26
# 26. Check whether project status is not completed
'''
project=input('Enter status:')
if not(project=='completed' ):
    print(True)
else:
    print(False)
'''

# Question 27
# 27. Check whether password is not correct
'''
name='satya'
passWord=input('Enter password:')
if not(passWord==name ):
    print(True)
else:
    print(False)
'''

# Question 28
# 28. Check whether temperature is not safe
'''
temp=input('Enter:')
if not(temp=='safe' ):
    print(True)
else:
    print(False)
'''

# Question 29
#29. Check whether selected option is not allowed
'''
option=input('Enter:')
if not(option=='allowed' ):
    print(True)
else:
    print(False)
'''

# Question 30
#30. Check whether marks are not passing marks
'''
marks=int(input('Enter marks:'))
if not(marks>=35 ):
    print(True)
else:
    print(False)
 '''
 