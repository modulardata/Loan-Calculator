import argparse
import math


class LoanCalculator:
    args = None

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--payment', type=float)
        parser.add_argument('--principal', type=int)
        parser.add_argument('--periods', type=int)
        parser.add_argument('--interest', type=float)
        self.args = parser.parse_args()
        self.calculate_user_input()

    def calculate_user_input(self):
        try:
            if self.args.payment is None:
                self.calculate_monthly_payment()
            elif self.args.principal is None:
                self.calculate_loan_principal()
            elif self.args.periods is None:
                self.calculate_months_to_pay()
        except Exception:
            print("Some necessary arguments are missed!")

    def calculate_months_to_pay(self):
        payment = self.args.payment
        principal = self.args.principal
        interest_rate = self.interest_rate()

        months_amount = math.ceil(math.log(payment / (payment - interest_rate * principal), 1 + interest_rate))

        years, months = divmod(months_amount, 12)

        if months > 0:
            years += months // 12
            months %= 12

        print(self.print_months_to_pay(years, months))

    def calculate_monthly_payment(self):
        principal = self.args.principal
        periods = self.args.periods
        interest_rate = self.interest_rate()
        result = math.ceil(principal * (interest_rate * pow(1 + interest_rate, periods)) / (
                pow(1 + interest_rate, periods) - 1))
        print(f'Your monthly payment = {result}!')

    def calculate_loan_principal(self):
        payments = self.args.payment
        periods = self.args.periods
        interest_rate = self.interest_rate()
        result = math.floor(payments / (interest_rate * pow(1 + interest_rate, periods) / (
                pow(1 + interest_rate, periods) - 1)))
        print(f'Your loan principal = {result}!')

    def interest_rate(self):
        interest = self.args.interest
        return interest / (12 * 100)

    @staticmethod
    def print_months_to_pay(years, months):
        years_str = f'{years} {"years" if years != 1 else "year"} ' if years != 0 else ''
        months_str = f'{months} {"months" if months != 1 else "month"}' if months != 0 else ''

        if years_str and months_str:
            middle_str = 'and '
        else:
            middle_str = ''

        return f'It will take {years_str}{middle_str}{months_str} to repay this loan!'


def main():
    LoanCalculator()


if __name__ == '__main__':
    main()
