# write a program to sort numbers 
def sort():
    numbers = [1,5,6,9,4,5,3,2]
    numbers.sort()
    return numbers

print(sort())

# Write a program to find the largest number in a list
def largestNumber():
    list = []
    for i in range(6):
        number = int(input("Enter Number"))
        list.append(number)
        largest = max(list)
    print("The largest number is:", largest)
largestNumber()
    

# Write a program to find the second largest number in a list
def secondLargestNumber():
    list = []
    for i in range(6):
        number = int(input("Enter Number: "))
        list.append(number)
    list.sort()
    secondLargestNumber = list[-2]
    print("Second largest number is: ", secondLargestNumber)

secondLargestNumber()

# Write a program to find the smallest number in a list
def smallestNumber():
    list = []
    for i in range(6):
        number = int(input("Enter Number: "))
        list.append(number)
        smallest = min(list)
    print("The smallest number is:", smallest)
smallestNumber()

# Write a program to find the sum of all numbers in a list
def sumOfList():
    list = []
    for i in range(5):
        number = int(input("Enter NuMber"))
        list.append(number)
    sumOfList = sum(list)
    print("The sum of all numbers in the list is:", sumOfList)
sumOfList()

# EXCEPTION HANDLING
# Write a program to handle division by zero exception

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Divisible by Zero is undefined")
finally:
    print("in finally block")


# Write a program to handle invalid input exception
try:
    num1 , num2 = int(input("Enter numbers with gaps or commas"))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Divisible by Zero is undefined")
except ValueError:
    print("Invalid input! Please enter numeric values only.")
except:
    print("Some other exception occurred")
else:
    print("No exception occurred")
finally:
    print("in finally block")