# while loops will execute a block of code while a condition is true

# continue makes the loop continue 
# break makes the loop stop  

# value = 1

# while value <= 10:
#     value += 1
#     if value == 5:   
#         continue 
#     print(value)
# else:
#     print(f"Value is now equal to {value}")

# # for loops
# names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# the x in the above for loop represents any character in the list

# for x in names:
#     if x == "Sarah":
#         break

# nested loops
# names = ["Dave", "Sara", "John"]
# actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

# Q1 - Sum of Natural Numbers
# Write a program that uses a for loop to calculate the sum of the first n natural numbers.
# (Example: If n = 5, the output should be 1 + 2 + 3 + 4 + 5 = 15.)
# n = int(input("Enter a number: "))
# total_sum = 0

# for x in range(1,n+1):
#     total_sum += x

# print(total_sum)



# Q2 - Even Numbers Up to N
# Use a while loop to print all even numbers from 1 to n.
# n = int(input("Please enter a number"))
# x = 1

# while x <= n:
#     if x % 2 == 0:
#         print(x)
#     x += 1

# Q3 - Factorial Calculation
# Write a program that calculates the factorial of a given number using a for loop.
# (Example: 5! = 5 × 4 × 3 × 2 × 1 = 120.)
# n = int(input("Please enter a number"))
# factorial = 1


# for x in range(1, n+1):
#     factorial *= x

# print(factorial)

# Q4 - Multiplication Table
# Ask the user for a number and use a for loop to print its multiplication table (up to 10).
# number = int(input("enter number"))
# result = 0 

# for x in range(1, 11):
#     result = number * x
#     print(f"{x} * {number} = {result}")


# Q5 - Guess the Number (While Loop)
# Write a program that repeatedly asks the user to guess a number until they guess correctly.
# (Hint: Use random.randint() to generate a random number.)
# import random

# guess = int(input("guess number "))
# answer = random.randint(1,10)

# while guess != answer:
#     if guess < answer:
#         print("Too low!")
#         guess = int(input("guess number "))
#     elif guess > answer:
#         print("Too high!")
#         guess = int(input("guess number "))

# print("Well done!")

# Q6 - Find Prime Numbers
# Write a program using a for loop to print all prime numbers between 1 and n.


# Ask the user for a number N and print all numbers from 1 to N.
# n = int(input("enter number "))
# result = []

# for x in range(1, n+1):
#     result.append(x)

# print(result)

# Ask the user for a number N and print all even numbers from 1 to N.
# n = int(input("enter number "))
# result = []

# for x in range(1, n+1):
#     if x % 2 == 0:
#         result.append(x)

# print(result)

# Ask the user for a number N and print the numbers from N down to 1.
# n = int(input("enter number "))
# result = []

# for x in range(n, 0, -1):
#     result.append(x)

# print(result)

# Ask the user for a number N and calculate the sum of numbers from 1 to N.
# n = int(input("enter number "))
# result = 0

# for x in range(1, n+1):
#     result += x

# print(result)

# Ask the user for a number N and calculate the factorial (N! = N × (N-1) × (N-2) × ... × 1).
# n = int(input("enter number "))
# result = 1

# for x in range(n,0,-1):
#     result *= x

# print(result)

# You have a list of column names. Write a loop to convert them all to lowercase.
# Expected Output: ["customer_id", "order_date", "sales_amount"]
# columns = ["Customer_ID", "Order_DATE", "SALES_AMOUNT"]
# result = []

# for x in columns: 
#     lowercase = x.lower()
#     result.append(lowercase)

# print(result)

# You have a dataset with missing values (None). Write a loop to count how many None values are in the list.

# data = [100, None, 250, 300, None, 400, None]
# result = 0

# for x in data:
#     if x == None:
#         result += 1
#     else:
#         continue 

# print(result)

# You have the same dataset with None values. Write a loop to create a new list that only contains the valid (non-None) values.
# data = [100, None, 250, 300, None, 400, None]
# result = []

# for x in data:
#     if x != None:
#         result.append(x)
#     else:
#         continue

# print(result)

# # Given a list of numbers write a loop to find the highest number.
# numbers = [10, 50, 20, 80, 60]
# max_value = numbers[0]

# for x in numbers:
#     if x > max_value:
#         max_value = x

# print(max_value)

# Write a loop to combine them into a dictionary. Expected Output: {"id": 101, "name": "Alice", "age": 25}
columns = ["id", "name", "age"]
values = [101, "Alice", 25]
dict = {}

for x in columns:
    for y in values:
        dict += (x, y)

print(dict)