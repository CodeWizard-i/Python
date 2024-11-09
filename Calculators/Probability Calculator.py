import time

print("Probability Calculator")
time.sleep(1)
print()

print("Values should be between 1 and 0.")
try:
    a = float(input("Probability of A = "))
    b = float(input("Probability of B = "))
    print()
    time.sleep(1)

    if not (0 <= a <= 1) or not (0 <= b <= 1):
        print("Values must be between 0 and 1!")
    else:
        print("Probability of A not occurring = ", 1 - a)
        print("Probability of B not occurring = ", 1 - b)
        print("Probability that A & B both occurring = ", a * b)
        print("Probability that A or B to both occur = ", (a + b) - (a * b))
        print("Probability that A or B occurs but not both = ", (a + b) - (2 * a * b))
        print("Probability of neither A nor B occuring = ", 1 - (a + b - (a * b)))
        print("Probability of A occurring but not B = ", a * (1 - b))
        print("Probability of B occurring but not A = ", (1 - a) * b)
except ValueError:
    print("Invalid Input")