import math
import argparse
import sys

def calculate_periods(principal, payment, interest_rate):
    if payment <= interest_rate * principal:
        return "The payment is too low to cover the interest. You will never repay the loan!"
    n = math.log(payment / (payment - interest_rate * principal), 1 + interest_rate)
    n = math.ceil(n)
    total_payment = payment * n
    overpayment = total_payment - principal
    years, months = divmod(n, 12)
    if years and months:
        return f"It will take {years} years and {months} months to repay this loan!\nOverpayment = {overpayment}"
    elif years:
        return f"It will take {years} year{'s' if years > 1 else ''} to repay this loan!\nOverpayment = {overpayment}"
    else:
        return f"It will take {months} months to repay this loan!\nOverpayment = {overpayment}"

def calculate_payment(principal, periods, interest_rate):
    annuity = principal * interest_rate * math.pow(1 + interest_rate, periods) / (math.pow(1 + interest_rate, periods) - 1)
    total_payment = math.ceil(annuity) * periods
    overpayment = total_payment - principal
    return f"Your annuity payment = {math.ceil(annuity)}!\nOverpayment = {overpayment}"

def calculate_principal(payment, periods, interest_rate):
    principal = payment * (math.pow(1 + interest_rate, periods) - 1) / (interest_rate * math.pow(1 + interest_rate, periods))
    total_payment = payment * periods
    overpayment = total_payment - principal
    return f"Your loan principal = {math.floor(principal)}!\nOverpayment = {overpayment}"

def calculate_differentiated_payments(principal, periods, interest_rate):
    total_payment = 0
    for m in range(1, periods + 1):
        diff_payment = (principal / periods) + interest_rate * (principal - (principal * (m - 1) / periods))
        diff_payment = math.ceil(diff_payment)
        total_payment += diff_payment
        print(f"Month {m}: payment is {diff_payment}")
    overpayment = total_payment - principal
    print(f"\nOverpayment = {overpayment}")

def main():
    parser = argparse.ArgumentParser(description="Loan Calculator", add_help=False)
    parser.add_argument("--type", help="Type of payment: annuity or differentiated")
    parser.add_argument("--principal", type=float, help="The loan principal amount")
    parser.add_argument("--periods", type=int, help="The number of months to repay the loan")
    parser.add_argument("--interest", type=float, help="The annual interest rate (required)")
    parser.add_argument("--payment", type=float, help="The monthly payment amount")

    try:
        args = parser.parse_args()
    except:
        print("Incorrect parameters")
        sys.exit()

    # Validate --type argument
    if args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        sys.exit()

    # Validate interest rate
    if args.interest is None or args.interest <= 0:
        print("Incorrect parameters")
        sys.exit()

    # Validate no negative values in arguments
    values = [args.payment, args.principal, args.periods, args.interest]
    if any(v is not None and v < 0 for v in values):
        print("Incorrect parameters")
        sys.exit()

    interest_rate = args.interest / (12 * 100)

    if args.type == "diff":
        # Differentiated payments require principal, periods, and interest
        if args.principal is None or args.periods is None or args.payment is not None:
            print("Incorrect parameters")
        else:
            calculate_differentiated_payments(args.principal, args.periods, interest_rate)
    elif args.type == "annuity":
        # Annuity payments require exactly 3 out of 4 arguments
        provided_args = sum(arg is not None for arg in [args.payment, args.principal, args.periods])
        if provided_args != 2:
            print("Incorrect parameters")
            return
        if args.periods is None:
            print(calculate_periods(args.principal, args.payment, interest_rate))
        elif args.payment is None:
            print(calculate_payment(args.principal, args.periods, interest_rate))
        elif args.principal is None:
            print(calculate_principal(args.payment, args.periods, interest_rate))
    else:
        print("Incorrect parameters")

if __name__ == "__main__":
    main()