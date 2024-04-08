import argparse
import math
import sys


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    annuity_payment = principal * (i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)
    return math.ceil(annuity_payment)


def calculate_loan_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    return math.floor(principal)


def calculate_differentiated_payments(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0
    for month in range(1, periods + 1):
        diff_payment = math.ceil((principal / periods) + i * (principal - (principal * (month - 1) / periods)))
        total_payment += diff_payment
        print(f'Month {month}: payment is {diff_payment}')
    return total_payment


def calculate_number_of_payments(principal, payment, interest):
    i = interest / (12 * 100)
    n = math.log(payment / (payment - i * principal), 1 + i)
    return math.ceil(n)


def main():
    # Custom error message for invalid arguments
    def error_message(message):
        print("Incorrect parameters")
        sys.exit()

    # Check if --type is provided and if it's a valid choice before parsing
    if '--type' in sys.argv:
        type_index = sys.argv.index('--type') + 1
        if type_index < len(sys.argv):
            type_value = sys.argv[type_index]
            if type_value not in ['annuity', 'diff']:
                print("Incorrect parameters")
                return

    parser = argparse.ArgumentParser(description="Loan Calculator", add_help=False)
    parser.error = error_message  # Override the default error method
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment")
    parser.add_argument("--principal", type=int, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of periods")
    parser.add_argument("--interest", type=float, help="Interest rate")
    parser.add_argument("--payment", type=int, help="Monthly payment (only for annuity)")

    try:
        args = parser.parse_args()
    except SystemExit:
        print("Incorrect parameters")
        return

    # Pre-validation for --type argument to ensure custom error message is used
    if '--type' in sys.argv:
        type_index = sys.argv.index('--type') + 1
        if type_index >= len(sys.argv) or sys.argv[type_index] not in ['annuity', 'diff']:
            error_message("Incorrect parameters")

    try:
        args = parser.parse_args()
    except SystemExit:
        # The custom error message will be printed by the overridden error method
        return

    # Basic validation
    if not args.type or not args.interest or (args.type == "diff" and args.payment) or len(sys.argv) < 5:
        print("Incorrect parameters")
        return

    if any(arg is not None and arg < 0 for arg in [args.payment, args.principal, args.periods, args.interest]):
        print("Incorrect parameters")
        return

    if args.type == "annuity":
        if args.principal and args.payment and args.interest and not args.periods:
            periods = calculate_number_of_payments(args.principal, args.payment, args.interest)
            years, months = divmod(periods, 12)
            if years > 0 and months > 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif years > 0:
                print(f"It will take {years} years to repay this loan!")
            elif months > 0:
                print(f"It will take {months} months to repay this loan!")
            overpayment = (args.payment * periods) - args.principal
            print(f"Overpayment = {overpayment}")
        elif args.payment and args.periods and args.interest and not args.principal:
            principal = calculate_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
            overpayment = (args.payment * args.periods) - principal
            print(f"Overpayment = {overpayment}")
        elif args.principal and args.periods and args.interest and not args.payment:
            annuity_payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your annuity payment = {annuity_payment}!")
            overpayment = (annuity_payment * args.periods) - args.principal
            print(f"Overpayment = {overpayment}")
    elif args.type == "diff":
        if args.principal and args.periods and args.interest:
            total_payment = calculate_differentiated_payments(args.principal, args.periods, args.interest)
            overpayment = total_payment - args.principal
            print(f"\nOverpayment = {overpayment}")


if __name__ == "__main__":
    main()
