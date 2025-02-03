# Loan Calculator

## Description

This loan calculator computes various parameters of an annuity-based loan, where a fixed sum of money is paid at regular intervals (monthly). The calculator can determine:

- The number of monthly payments required to repay the loan.
- The monthly payment amount.
- The loan principal.
- The total loan interest.

The program works via command-line arguments, where you specify known values, and the calculator computes the missing parameter.

## Formulae Used

1. **Monthly Payment (Annuity Payment, A):**
   \[ A = P \times \frac{i (1 + i)^n}{(1 + i)^n - 1} \]
2. **Loan Principal (P):**
   \[ P = A \times \frac{(1 + i)^n - 1}{i (1 + i)^n} \]
3. **Number of Monthly Payments (n):**
   \[ n = \log\_{(1+i)} \left(\frac{A}{A - iP} \right) \]

Where:

- **A** = annuity (monthly payment)
- **P** = loan principal
- **i** = nominal monthly interest rate (annual interest rate / 12 / 100)
- **n** = number of months (loan term)

## Usage

Run the program using the command line with the appropriate arguments:

```
python creditcalc.py --principal=VALUE --payment=VALUE --periods=VALUE --interest=VALUE
```

- `--principal`: Loan principal amount.
- `--payment`: Monthly payment amount.
- `--periods`: Number of months to repay the loan.
- `--interest`: Annual interest rate (without `%`).

### Note:

- The program cannot calculate the interest rate; it must always be provided.
- The missing parameter is computed based on the provided values.
- The number of months is converted into years and months for readability.

## Examples

### Example 1: Calculating the number of payments

```sh
python creditcalc.py --principal=1000000 --payment=15000 --interest=10
```

**Output:**

```
It will take 8 years and 2 months to repay this loan!
```

### Example 2: Calculating the monthly payment

```sh
python creditcalc.py --principal=1000000 --periods=60 --interest=10
```

**Output:**

```
Your monthly payment = 21248!
```

### Example 3: Calculating the loan principal

```sh
python creditcalc.py --payment=8721.8 --periods=120 --interest=5.6
```

**Output:**

```
Your loan principal = 800000!
```

## Installation

No installation is required beyond Python. Simply run the script using Python 3.

## License

This project is released under the MIT License.
