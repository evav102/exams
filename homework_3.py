#0
number = (int(input("Please type your number: ")))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#1
total = 0
for num in range(1,101):
    if num % 2 == 0:
        total += num
print(f"The sum of all even numbers is {total}")

#2
while True:
    number = int(input("How much is 5 + 12: "))
    if number != 17:
        print("Try again")
    else:
        print("Correct")
        break


#3

for num in range(1, 1001):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

#4
import random

computer_number = random.randint(1, 101)

print("What number i'm thinking between 1 and 100?: ")
while True:
    user_number = int(input("Type your number: "))
    user_number += 1

    if user_number == computer_number:
        print("Correct")
        break
    elif user_number < computer_number:
        print("Too low.Try again")
    elif user_number > computer_number:
        print("Too high. Try again")


#6
number = int(input("Enter a number: "))

# Print the multiplication table using a for loop
print("Multiplication Table for", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

#7
number = int(input("Enter a number: "))
if number <= 1:
    print("Number is not a prime number")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")

#8
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    # Inner loop for columns
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
