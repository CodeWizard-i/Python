import math
import time

print("Fraction Calculator")
time.sleep(1)
print()

print("Type the number of the option.")
time.sleep(1)
print()

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Equivalent")

time.sleep(1)
print()

a = input("Type the number = ")
time.sleep(1)
print()

if a == '1' :
 print("Addition")
 time.sleep(1)
 print()
 b = int(input("Numerator = "))
 c = int(input("Denominator = "))
 print()
 time.sleep(1)
 d = int(input("Numerator = "))
 e = int(input("Denominator = "))
 print()
 time.sleep(1)
 f = (math.lcm(c,e)/c)*b
 g = (math.lcm(c,e)/e)*d
 h = math.gcd(int(f+g),math.lcm(c,e))
 i = (f+g)/h
 j = math.lcm(c,e)/h
 print("Numerator = ", i)
 print("Denominator = ", j)
 
elif a == '2' :
 print("Subtraction")
 time.sleep(1)
 print()
 b = int(input("Numerator = "))
 c = int(input("Denominator = "))
 print()
 time.sleep(1)
 d = int(input("Numerator = "))
 e = int(input("Denominator = "))
 print()
 time.sleep(1)
 f = (math.lcm(c,e)/c)*b
 g = (math.lcm(c,e)/e)*d
 h = math.gcd(int(f-g),math.lcm(c,e))
 i = (f-g)/h
 j = math.lcm(c,e)/h
 print("Numerator = ", i)
 print("Denominator = ", j)
 
elif a == '3' :
 print("Multiplication")
 time.sleep(1)
 print()
 b = int(input("Numerator = "))
 c = int(input("Denominator = "))
 print()
 time.sleep(1)
 d = int(input("Numerator = "))
 e = int(input("Denominator = "))
 f = int(float(b)) * int(float(d))
 g = int(float(c)) * int(float(e))
 h = math.gcd(int(f), int(g))
 print()
 time.sleep(1)
 print("Numerator = ", f/h)
 print("Denominator = ", g/h)

elif a == '4' :
 print("Division")
 time.sleep(1)
 print()
 b = int(input("Numerator = "))
 c = int(input("Denominator = "))
 print()
 time.sleep(1)
 d = int(input("Numerator = "))
 e = int(input("Denominator = "))
 f = int(float(b)) * int(float(e))
 g = int(float(c)) * int(float(d))
 h = math.gcd(int(f), int(g))
 print()
 time.sleep(1)
 print("Numerator = ", f/h)
 print("Denominator = ", g/h)

elif a == '5' :
 print("Equivalent")
 time.sleep(1)
 print()
 b = int(input("Numerator = "))
 c = int(input("Denominator = "))
 print()
 time.sleep(1)
 d = int(input("Times = "))
 print()
 time.sleep(1)
 print("Numerator = ", b*d)
 print("Denominator = ", c*d)

else:
 print("Invalid Option")