# write your code here
# Enter the loan principal:
print("Enter the loan principal:")
principalAmount = int(input())

print("What do you want to calculate?")
print("type \"m\" for number of monthly payments,")
print("type \"p\" for the monthly payment:") 
typePayment = input()
repayments = 0
if (typePayment == "m"):
        print("Enter the monthly payment:")
        monthlyPayments = int(input())
        repayments= principalAmount // monthlyPayments
        print(f"It will take {repayments} months to repay the loan")
elif (typePayment == "p"):
        print("Enter the number of months:")
        months = int(input())
        basePay = principalAmount // (months)
        repayments = principalAmount - (months - 1) * basePay
        if (principalAmount % months == 0):
            print(f"Your monthly payment = {basePay}")
        else: 
            print(f"Your monthly payment = {basePay + 1} and the last payment = {repayments}")