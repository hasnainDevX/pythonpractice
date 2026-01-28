# # write a program to sort numbers 
# def sort():
#     numbers = [1,5,6,9,4,5,3,2]
#     numbers.sort()
#     return numbers

# print(sort())

# # Write a program to find the largest number in a list
# def largestNumber():
#     list = []
#     for i in range(6):
#         number = int(input("Enter Number"))
#         list.append(number)
#         largest = max(list)
#     print("The largest number is:", largest)
# largestNumber()
    

# # Write a program to find the second largest number in a list
# def secondLargestNumber():
#     list = []
#     for i in range(6):
#         number = int(input("Enter Number: "))
#         list.append(number)
#     list.sort()
#     secondLargestNumber = list[-2]
#     print("Second largest number is: ", secondLargestNumber)

# secondLargestNumber()

# # Write a program to find the smallest number in a list
# def smallestNumber():
#     list = []
#     for i in range(6):
#         number = int(input("Enter Number: "))
#         list.append(number)
#         smallest = min(list)
#     print("The smallest number is:", smallest)
# smallestNumber()

# # Write a program to find the sum of all numbers in a list
# def sumOfList():
#     list = []
#     for i in range(5):
#         number = int(input("Enter NuMber"))
#         list.append(number)
#     sumOfList = sum(list)
#     print("The sum of all numbers in the list is:", sumOfList)
# sumOfList()

# # EXCEPTION HANDLING
# # Write a program to handle division by zero exception

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print("The result is:", result)
# except ZeroDivisionError:
#     print("Divisible by Zero is undefined")
# finally:
#     print("in finally block")


# # Write a program to handle invalid input exception
# try:
#     num1 , num2 = int(input("Enter numbers with gaps or commas"))
#     result = num1 / num2
#     print("The result is:", result)
# except ZeroDivisionError:
#     print("Divisible by Zero is undefined")
# except ValueError:
#     print("Invalid input! Please enter numeric values only.")
# except:
#     print("Some other exception occurred")
# else:
#     print("No exception occurred")
# finally:
#     print("in finally block")


# Dictionary Operations
# Write a program to add a key-value pair to a dictionary

# def addKeyValuePair():
#     my_dict = {}
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     my_dict[key] = value
#     print("Updated dictionary:", my_dict)
# addKeyValuePair()

# def addKeyValuePair(key, value):
#     my_dict = {}
#     my_dict[key] = value
#     print("Updated dictionary:", my_dict)
# addKeyValuePair("name", "Alice")


# def addKeyValuePair(key, value):
#     my_dict = {}
#     my_dict[key] = value
#     print("Updated dictionary:", my_dict)
# addKeyValuePair("name", "Alice")

# def makeDic():
#     try:
#         dict = {}
#         diclength = int(input("Enter Dictionary length from 1-10"))

#         if diclength <= 0 or diclength > 10:
#             raise ValueError("value must be greater than zero and less than equals to 10")
#     except ValueError as ve:
#         print("Invalid input:", ve)
#     else: 
#         for i in range(diclength):
#             key, value = input("Enter key value separted by gaps or commas").split()
#             dict[key] = value
#     print("The dictionary is:", dict)
# makeDic()


# Write a program to remove a key-value pair from a dictionary
# def removeDicItem():
#     dict = {"name": "hasnain", "age":18, "bodycount": 0}
#     print(dict)
#     item = input("Enter item you want to remove")
#     if item in dict:
#         del dict[item]
#     print("Updates Dictionary", dict)

# removeDicItem()

