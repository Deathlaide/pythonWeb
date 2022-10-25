import math

def isPrime(value):
    if value == 0 or value > 100000:
        return "Incorrect input"
    elif value == 1:
        return True
    else:
        for i in range(2, 100000):
            if i != value and value%i == 0:
                return False
            elif i > value:
                return True

number = int(input("Enter a number: "))
print(isPrime(number))

