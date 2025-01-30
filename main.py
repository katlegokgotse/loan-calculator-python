# write your code here
# Enter the loan principal:
import math
print("Enter the loan principal:")
principalAmount = int(input())

print("What do you want to calculate?")
print("type \"m\" for number of monthly payments,")
print("type \"p\" for the monthly payment:") 
typePayment = input()
if (typePayment == "m"):
        print("Enter the monthly payment:")
        monthlyPayments = int(input())
        repayments= principalAmount / monthlyPayments
        if principalAmount % monthlyPayments != 0:
            repayments +=1
        print(f"It will take {math.floor(repayments)} months to repay the loan")
elif (typePayment == "p"):
        print("Enter the number of months:")
        months = int(input())
        basePay = principalAmount / months
        lastPayment = 0
        lastPayment = principalAmount - (math.ceil(basePay) * (months - 1))
        if (principalAmount % months == 0):
            print(f"Your monthly payment = {basePay}")
        else: 
            print(f"Your monthly payment = {math.ceil(basePay)} and the last payment = {lastPayment}")