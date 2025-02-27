# users = ["Dave", "John", "Sara"]

# # print(users[0:])

# # print(len(users))

# data = ["Sad", 42, True]

# # users.extend(data)
# # print(users)

# # this allows you to choose at what point you add something to your list, in this case, 'Bob' is added at position 0
# users.insert(0, "Bob") 
# print(users)

# # allows you to add multiple entries to a particulat spot
# users[2:2] = ["Eddie", "Alex"]
# print(users)

# # this is called a slice. removes original values in position 1 and 2 and replaces with the list below
# users[1:3] = ["Robert", 'JPJ']
# print(users)

# tuples - the data inside the tuple will not change and the order of the data inside it wont change either
# it uses () instead of []

# practice qs using chatGPT

# Write a Python program to create a list of five numbers and print the third element.
# my_list = [2,4,6,8,10]
# print(my_list[2])


# Write a program to add an element 10 to the end of the list [1, 2, 3, 4].
# my_list = [1,2,3,4]
# my_list += [10]
# print(my_list)

# Given a list nums = [10, 20, 30, 40], write code to change the second element to 25.
# nums = [10, 20, 30, 40]
# nums[1] = 25
# print(nums)

# Write a Python program to find the length of a tuple (10, 20, 30, 40, 50).
# example_tuple = (10, 20, 30, 40, 50)
# print(len(example_tuple))


# Create a list of numbers and use a loop to print only the even numbers from it.
# nums = [1,2,3,4,5,6,7,8,9,10]

# for x in nums:
#     if x % 2 == 0:
#         print(x)
#     else:
#         continue


# Convert the list [‘apple’, ‘banana’, ‘cherry’] into a tuple.
# fruits = ["apple", "banana", "cherry"]
# fruits_tuple = tuple(fruits)          
# print(type(fruits_tuple))

# Given a tuple t = (1, 2, 3, 4, 5), write code to get the sum of all its elements.
# t = (1,2,3,4,5)
# total_sum = 0

# for x in t:
#     total_sum += x

# print(total_sum)

# Reverse the list [10, 20, 30, 40, 50] using a Python function.
nums = [10,20,30,40,50]
nums.sort(reverse=True)
print(nums)