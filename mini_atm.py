#Github: DimIsCoding
import os
budget = 6666


print("Welcome to FinanceBank ATM!\n")
print("1 - View Budget\n")
print("2 - Withdraw Money \n")
print("3 - Deposit Money \n")
print("4 - Exit")
option = int(input(":"))

if option == 1:
    print(f"Your Updated Budget:", budget)
    breakpoint
if option == 2:
    withdrawn_amount = int(input("Enter the amount of money you want to withdraw: "))
    if withdrawn_amount > budget:
        print("You can't withdraw more money than your current budget!")
    if withdrawn_amount < budget:
        print("Your Remaining Budget:",budget-withdrawn_amount)
    breakpoint
if option == 3:
    deposited_amount= int(input("Enter the amount of money you want to deposit: "))
    print("Your Updated Budget:", budget+deposited_amount)
if option == 4:
    print("Checking Out from  your Account....\n")
    print("Check Out Completed,Have a Good Day!\n")
    os.system("pause")
elif option != 1 and 2 and 3 and 4:
    print("Please select a valid option.")

