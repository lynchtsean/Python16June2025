print ("Hello, world!")
print (1,2,3,4,5,6,7,8,9,10)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Sum is:",a + b)
      
num = int(input("Enter a number:"))
print("Even")

import random
print("Random number:", random.randint(1, 100))

import random
 
print(" Welcome to the Guessing Game!")
secret_number = random.randint(1, 10)
attempts = 3
 
while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("🎉 Correct! You win!")
        break
    else:
        attempts -= 1
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
 
        if attempts > 0:
            print(f"Try again! {attempts} attempts left.")
        else:
            print(f" Out of tries! The number was {secret_number}.")

for i in range(1,1000):
    print(i)

name = input("What is your name?")
job = input("Thank you, what is your job? ")
salary = input("What is your salary? ")
location = input("Where are you located?")

print(f"I, {name}, from {location}, working as a {job}, with the salary of {salary}, would love to work in cloud and AI.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers from 1 to 1000 are:")
for number in range(1, 1001):
    if is_prime(number):
        print(number)

n = int(input("Enter how many Fibonacci numbers to print: "))
a = 0
b = 1
for i in range(n):
   print(a)
   next = a + b
   a = b
   b = next