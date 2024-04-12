#1
print("Hello World")

#2
name = "Eva"
age = 30
color = "blue"
print(f"My name is {name}, I am {age} years old, and my favorite color is {color}.")

#3
lenght = int(input("Type the lenght: "))
width = int(input("Type the width: "))
area = lenght * width
print(f"The area of rectngre is {area}")

#4
fahrenheit = int(input("Type temperature in Fahrenheit: "))
a = fahrenheit - 32
b = 5 * a
c = b / 9
print(f"Temperature in Celsius is {c:.2f}")


#5
first_number = int(input("Enter your first number:"))
second_number = int(input("Enter your second number: "))
sum = first_number + second_number
print(f"The sum is {sum}")
difference = first_number - second_number
print(f"The difference is {difference}")
product = first_number * second_number
print(f"The products is {product}")
quotient = first_number / second_number
print(f"The quotient is {quotient}")


#6


#7
number = int(input("Please type your first number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#8
age = int(input("Please enter your age: "))
if age >= 18:
    print("Please select your vote")
else:
    print("Sorry, you are not able to vote.")

#9
your_string = input("Please enter a city: ")
lenght = len(your_string)
print(f"The lenght of the city is {lenght} symbols")

#10
first_name = input("Please, enter your first name: ")
last_name = input("Type your last name: ")
print(f" Your name is {first_name} {last_name}.")