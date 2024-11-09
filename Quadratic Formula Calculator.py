import math
import time

print("Quadratic Formula Calculator")
print()
time.sleep(1)

print("NOTE : This formula will give an integer value when ax² + bx + c = 0")
print()
time.sleep(1)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print()
time.sleep(1)

d = (b**2) - (4*a*c)
e = (-b + math.sqrt(d))/(2*a)
f = (-b - math.sqrt(d))/(2*a)

if a*e**2 + b*e + c == a*f**2 + b*f + c :
 print("First Solution = ", e)
 print("Second Solution = ", f)

else :
 print("ax² + bx + c is not equal to 0!")