# A small mobile recharge shop wants a simple computer program to help the shopkeeper calculate bills and avoid manual mistakes.
# The shopkeeper offers the following services:
# Mobile Recharge
# Internet Package
# Utility Bill Payment
# Each customer can choose one service at a time.

# 🧾 Program Requirements
# Write a Python program that helps the shopkeeper with the following:
# When the program starts, display a welcome message and show a menu of services:
# 1) Mobile Recharge
# 2) Internet Package
# 3) Utility Bill Payment
# 4) Exit

# Ask the customer to choose a service by entering a number.
# For every service:
# Ask for the amount
# Apply a service charge:
# Mobile Recharge → 2% charge
# Internet Package → 5% charge
# Utility Bill → 3% charge
# Calculate the total bill using operators
# After displaying the total bill:
# Ask if the shopkeeper wants to serve another customer
# Use a loop to repeat the process
# Use exception handling to:
# Handle non-numeric input for amount
# Handle invalid menu choices
# Prevent program crash
# The program should only stop when Exit is selected.

def main():
    print("Welcome to the Mobile Recharge Shop!")
    print("Please choose a service: \n 1) Mobile Recharge \n 2) Internet Package \n 3) Utility Bill Payment \n 4) Exit")
    while True:
        try:
            options = [1,2,3,4]
            option = int(input('Enter service number'))
            if option not in options:
                raise ValueError("Please choose between 1-4")
            elif option == 4:
                print("Exiting Good bye!")
                break
            elif option == 1:
                print("Mobile Recharge Service")
                amount = float(input("Enter the amount for Mobile Recharge: "))
                serviceCharge = 0.02 * amount
                totalBill = amount + serviceCharge
                print(f'Your Total bill is ${totalBill:.2f}')
            elif option == 2:
                print("Internet Package Service")
                amount = float(input("Enter the amount for Internet Package: "))
                serviceCharge = 0.05 * amount
                totalBill = amount + serviceCharge
                print(f"Your total Bill is ${totalBill:.2f}")
            elif option == 3:
                print("Utility Bill Payment")
                amount = float(input("Enter the amount for the Utility Bill Payment"))
                serviceCharge = 0.03 * amount
                totalBill = amount + serviceCharge
                print(f"Your total bill is ${totalBill}")
            else:
                print("Enter valid input")
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
        again = input("Do you want to serve another customer? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting. Thank you!")
            break
main()
