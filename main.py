# write your code here
# Enter the loan principal:
print("Enter the loan principal:")
principalAmount = int(input())

print("What do you want to calculate?")
typePayment = input()
repayments = 0
while True:
    if (typePayment == "m"):
        print("Enter the monthly payment:")
        monthlyPayments = int(input())
        repayments= principalAmount // monthlyPayments
        print(f"It will take {repayments} months to repay the loan")
    elif (typePayment == "p"):
        print("Enter the number of months:")
        months = int(input())
        payments 
        repayments = principalAmount - (months - 1) * 
        print(f"Your monthly payment = {repayments}")
    print("What do you want to calculate?")
    typePayment = input()


#Formula : principal−(periods−1)⋅payment