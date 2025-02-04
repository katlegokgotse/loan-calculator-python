import math
import argparse

def calculate_periods(principal, payment, interest_rate):
    if payment <= interest_rate * principal:
        return "The payment is too low to cover the interest. You will never repay the loan!"
    n = math.log(payment / (payment - interest_rate * principal), 1 + interest_rate)
    n = math.ceil(n)
    years, months = divmod(n, 12)
    if years and months:
        return f"It will take {years} years and {months} months to repay this loan!"
    elif years:
        return f"It will take {years} year{'s' if years > 1 else ''} to repay this loan!"
    else:
        return f"It will take {months} months to repay this loan!"

def calculate_payment(principal, periods, interest_rate):
    annuity = principal * interest_rate * math.pow(1 + interest_rate, periods) / (math.pow(1 + interest_rate, periods) - 1)
    return f"Your monthly payment = {math.ceil(annuity)}!"

def calculate_principal(payment, periods, interest_rate):
    principal = payment * (math.pow(1 + interest_rate, periods) - 1) / (interest_rate * math.pow(1 + interest_rate, periods))
    return f"Your loan principal = {math.floor(principal)}!"

def main():
    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument("--principal", type=float, help="The loan principal amount")
    parser.add_argument("--periods", type=int, help="The number of months to repay the loan")
    parser.add_argument("--interest", type=float, required=True, help="The annual interest rate (required)")
    parser.add_argument("--payment", type=float, help="The monthly payment amount")
    args = parser.parse_args()

    interest_rate = args.interest / (12 * 100)

    if args.principal is not None and args.periods is not None and args.payment is not None:
        print("Incorrect parameters. Please provide exactly three of the four arguments.")
    elif args.periods is None and args.principal is not None and args.payment is not None:
        print(calculate_periods(args.principal, args.payment, interest_rate))
    elif args.payment is None and args.principal is not None and args.periods is not None:
        print(calculate_payment(args.principal, args.periods, interest_rate))
    elif args.principal is None and args.payment is not None and args.periods is not None:
        print(calculate_principal(args.payment, args.periods, interest_rate))
    else:
        print("Incorrect parameters. Please provide exactly three of the four arguments.")

if __name__ == "__main__":
    main()