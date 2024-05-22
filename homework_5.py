
#1
numbers = list(range(1, 101))
print(numbers)


#2
numbers = list(range(1, 101))
reversed_numbers = numbers[::-1]
print(reversed_numbers)

#3
items = ["milk", "meat", "juice", "tomatoes,", "bread"]
print(len(items))

items = ["milk", "meat", "juice", "tomatoes,", "bread"]
item_lengths = [len(word) for word in items]
print(item_lengths)


#4
def sum_even_numbers(list):
    return sum(num for num in list if num % 2 == 0)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
result = sum_even_numbers(list)
print("Sum of even numbers is:", result)

#5
numbers = (1, 2, 33, 14, 28, 87)


#7
students = {
    "Ana": ["34536", "1234"],
    "Bobi": ["453111", "4444"],
    "Clara": ["4444", "4563", "43456"]
}

ana_accounts = students.get("Ana", [])
print("John's bank account numbers:", ana_accounts)


bobi_accounts = students.get("Bobi", [])
print("Alice's bank account numbers:", bobi_accounts)


clara_accounts = students.get("Clara", [])
print("Bob's bank account numbers:", clara_accounts)


#10
set_1 = {2, 5, 7, 1, 4, 6, 8}
set_2 = {5, 1, 4, 11, 9}

intersection = set_1.intersection(set_2)
print("Intersection of set1 and set2 is:", intersection)

#11
x = {"milk", "honey", "apples"}
y = {"bread", "pineapple", "tomatoes", "apples", "honey", "milk"}

z = x.issubset(y)
print(z)


#12
def remove_duplicates(input_list):
    new_set = set(input_list)
    return new_set


x = ["lion", "rabbit", "tiger", "snake", "horse", "lion", "cat", "tiger", "tiger"]
print("The original list is:", x)

new_list = remove_duplicates(x)
print("List after removing duplicates:", new_list)

#13
square = [x**2 for x in range(1, 31) if x % 2 == 0]
print(square)

#14
new_list = ["house", "car", "planet", "beach"]

lengths = {word: len(word) for word in new_list}
print(lengths)


#15
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = {n for n in range(2, 100) if prime_number(n)}
print(prime_numbers)