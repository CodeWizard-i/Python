import time

print("Prime Numbers")
print()
a = int(input("What is the maximum value you want to calculate ? "))
print()
      
nums = range(2,a)

def is_prime(num):
 for x in range(2, num):
  if (num % x) == 0:
   return False
 return True

time.sleep(2)

primes = list(filter(is_prime, nums))
print(primes)