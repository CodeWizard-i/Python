import math
import time

print("Calculator")
time.sleep(1)
print()

print("Type the number of the option.")
time.sleep(1)
print()

print("1 - Addition (x+y) ")
print("2 - Subtraction (x-y)")
print("3 - Multiplication (xy)")
print("4 - Division (x/y)")
print("5 - Factorial (x!)")
print("6 - Root (x^(1/y))")
print("7 - Exponentiation (x^y)")
print("8 - Log (logᵧ(x))")
print("9 - Floor(x) & Ceiling(x)")
time.sleep(1)
print()

a = input("Type the number = ")
time.sleep(1)
print()

if a =='1' :
 print("Addition (x+y)")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("x+y =",x+y)

elif a =='2' :
 print("Subtraction (x-y)")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("x-y =",x-y)

elif a =='3' :
 print("Multiplication (xy)")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("xy =",x*y)

elif a =='4' :
 print("Division (x/y)")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("x/y =",x/y)

elif a =='5' :
 print("Factorial (x!)")
 time.sleep(1)
 print()
 x = int(input("x = "))
 time.sleep(1)
 print()
 
 print("x! =",math.factorial(x))

elif a =='6' :
 print("Root (x^(1/y))")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("x^(1/y) =",x**(1/y))

elif a =='7' :
 print("Exponentiation (x^y)")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("x^y =",x**y)

elif a =='8' :
 print("Log (logᵧ(x))")
 time.sleep(1)
 print()
 x = float(input("x = "))
 y = float(input("y = "))
 time.sleep(1)
 print()
 
 print("logᵧ(x) =",math.log(x,y))

elif a =='9' :
 print("Floor(x) & Ceiling(x)")
 time.sleep(1)
 print()
 x = float(input("x = "))
 time.sleep(1)
 print()
 
 print("Floor(x) =",math.floor(x))
 print("Ceiling(x) =",math.ceil(x))

else :
 print("Invalid Option")