import math
  #in,not in -membership operators
a=[1,2,3,4]
if 2 in a:
      print(True)
if 34 not in a:
      print(False)
for i in range(1,10):
      print(True)
else:
  print(False)  
  #Logical operators
a = int(input("Enter first marks: "))
b = int(input("Enter second marks: "))

if a >= 35 and b >= 35:
    print("Pass in both subjects")

if a >= 35 or b >= 35:
    print("Pass in at least one subject")
    a = 20

if not a < 10:
    print("Condition TRUE")