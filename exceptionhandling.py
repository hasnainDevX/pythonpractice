
# 1. Write a program to make a basic calculator for kids in
# super market so that they may verify their calculation using Exceptional Handling. This program must 
# have all four arithmetic operations.

def basicCalculator():
    print("BASIC CALCULATOR")
    try:
        choice = int(input("Choose your operation number \n 1) + \n 2) - \n 3) / \n 4) * \n"))
        num1 = eval(input("Enter num1"))
        num2 = eval(input("Enter num2"))
        if type(num1) and type(num2) is not int:
            raise TypeError("Numbers can only be integer or float")
        if choice == 1:
            result = num1 + num2
            print(result) 
        elif choice == 2:
            result = num1 - num2
            print(result) 
        elif choice == 3:
            result = num1 / num2
            print(result) 
        elif choice == 4:
            result = num1 * num2
            print(result) 
        else:
            print("Invalid operation choice")
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except TypeError as e:
        print(e)
    except Exception:   
        print("Please Enter valid input")
    finally:
        print("Program Complete")

basicCalculator()