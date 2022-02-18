from math import floor, ceil, log
import argparse

# write your code here
parser = argparse.ArgumentParser(description="Calculates differentiated payments")
parser.add_argument('--type', choices=['annuity', 'diff'], required=True)
parser.add_argument('--principal', type=int, help="Loan amount collected.")
parser.add_argument('--periods', type=int, help="Number of months")
parser.add_argument('--interest', type=float, help="Interest in Percentage(without %)")
parser.add_argument('--payment', type=int, help="Monthly payment")

args = parser.parse_args()
if not args.interest or args.type == 'diff' and args.payment:
    print("Incorrect parameters")
    exit()

# Number of months in a calendar year
MONTHS_PER_YEAR = 12


def run(arguments) -> None:
    principal = arguments.principal
    periods = arguments.periods
    interest = get_nominal_interest(arguments.interest)
    payment = arguments.payment

    if arguments.type == 'annuity':
        calc_annuity(interest, principal, periods, payment)
    if arguments.type == 'diff':
        calc_diff(interest, principal, periods)


def calc_diff(interest, principal, periods) -> None:
    if not interest or not principal or not periods:
        print("Incorrect parameters")
        exit()
    monthly_payments = {}
    total_payments = 0
    for m in range(periods):
        m += 1
        monthly_payments[m] = mth_diff_payment(interest, principal, periods, m)
    for m, payment in monthly_payments.items():
        total_payments += payment
        print(f"Month {m}: payment is {payment}")
    print()
    print_if_overpaid(principal, total_payments)


def mth_diff_payment(interest, principal, periods, m) -> int:
    return ceil((principal / periods) + interest * (principal - ((principal * (m - 1)) / periods)))


def calc_annuity(interest, principal, periods, payment) -> None:
    if principal and periods:
        annuity_monthly_payment(principal=principal, period=periods, interest=interest)
    elif principal and payment:
        num_of_month(principal=principal, monthly_repayment=payment, interest=interest)
    elif payment and periods:
        loan_principal(interest=interest, period=periods, annuity=payment)
    else:
        print("Incorrect parameters")


def get_year_month_string_from_months(months: int) -> str:
    if months == 1:
        return f"{months} month"
    elif months < MONTHS_PER_YEAR:
        return f"{months} months"
    elif months == MONTHS_PER_YEAR:
        return "1 year"
    else:
        years = floor(months / MONTHS_PER_YEAR)
        remainder = months % MONTHS_PER_YEAR
        suffix = ""
        if remainder > 0:
            suffix = f" and {remainder} month{'s' if remainder > 1 else ''}"
        return "{years} year{plural}{suffix}".format(years=years, suffix=suffix, plural='s' if years > 1 else '')


def num_of_month(principal, monthly_repayment, interest) -> None:
    months = ceil(log((monthly_repayment / (monthly_repayment - interest * principal)), 1 + interest))
    print("It will take {period} to repay this loan!".format(period=get_year_month_string_from_months(months)))
    print_if_overpaid(principal, monthly_repayment * months)


def annuity_monthly_payment(principal, period, interest) -> None:
    monthly_repayment = ceil(principal * (interest * pow(1 + interest, period)) / (pow(1 + interest, period) - 1))
    print(f"Your annuity payment = {monthly_repayment}!")
    print_if_overpaid(principal, monthly_repayment * period)


def loan_principal(annuity, period, interest) -> None:
    principal = annuity / ((interest * pow(1 + interest, period)) / (pow(1 + interest, period) - 1))
    print(f"Your loan principal = {principal}!")
    print_if_overpaid(principal, annuity * period)


def get_nominal_interest(interest: float) -> float:
    return interest / 100 / 12


def print_if_overpaid(principal: int, paid: float):
    if paid > principal:
        print("Overpayment= {}".format(round(paid - principal)))


run(arguments=args)
