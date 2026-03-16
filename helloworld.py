import time

print("hello this is my first python program")

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print("The factorial of 5 is", factorial(5))

while True:
    time.sleep(10)
