import math


def menu():
    loan_amount = int(input("Enter the load principal:\n"))
    user_selection = input("What do you want to calculate?\ntype 'm' - for the number of monthly payments,\n"
                           "type 'p' - for the monthly payment:\n")
    if user_selection == "m":
        number_of_monthly_payments(loan_amount)
    else:
        monthly_payment(loan_amount)


def number_of_monthly_payments(loan_amount):
    monthly_payment_amount = int(input("Enter the monthly payment:\n"))
    total_months = (loan_amount + monthly_payment_amount - 1) // monthly_payment_amount
    print(f"It will take {total_months}", "months" if total_months > 1 else "month", "to repay the loan")


def monthly_payment(loan_amount):
    number_of_months = int(input("Enter the number of months:\n"))
    payment = math.ceil(loan_amount / number_of_months)
    payment_last = loan_amount - (number_of_months - 1) * payment
    print(f"Your monthly payment = {payment}",
          f"and the last payment = {payment_last}." if payment_last != payment else '')


menu()
