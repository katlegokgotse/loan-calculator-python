# write your code here
print("Enter the loan principal:")
principalAmount = int(input())
print("Enter the monthly payment:")
monthlyPayments = int(input())
repayments = principalAmount // monthlyPayments
print(f"It will take {repayments} months to repay the loan")