import argparse
import math

parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()

para = [args.principal, args.periods, args.interest, args.payment]
list_type = ["diff", "annuity"]
diff_list = []
diff_para = [args.principal, args.periods, args.interest]

if para.count(None) > 1:
    print("Incorrect parameters.")

elif args.type not in list_type or None:
    print("Incorrect parameters.")

elif args.interest == None:
    print("Incorrect parameters.")

elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters.")
    i = (args.interest/100)/12
    for c_month in range(args.periods):
        c_month += 1
        diff_pay = math.ceil((args.principal/args.periods) + i * (args.principal-((args.principal*(c_month-1))/args.periods)))
        diff_list.append(diff_pay)
        print(f"Month {c_month}: payment: {diff_pay}")
    print()
    diff_total = sum(diff_list)
    overpayment = diff_total - args.principal
    print(f"Overpayment = {round(overpayment)}")

elif args.type == "annuity":

    if args.principal is None:
        i = (args.interest/100)/12
        principal = args.payment/((i*math.pow(1+i, args.periods))/(math.pow(1+i, args.periods)-1))
        principal = math.floor(principal)

        print(f'Your loan principal = {principal}!')
        overpayment = (args.payment*args.periods - principal)
        print(f"Overpayment = {round(overpayment)}")

    elif args.periods is None:
        i = float((args.interest/100)/12)
        periods = math.log(args.payment/(args.payment-(i*args.principal)), 1+i)
        periods = math.ceil(periods)

        if periods % 12 == 0:
            y = periods//12
            print(f'It will take {y} years to repay this loan!')
        else:
            y = periods//12
            z = periods % 12
            if y == 0:
                print(f'It wil take {z} months to repay the loan!')
            elif y == 1:
                print(f'It will take {y} year and {z} months to repay the loan!')
            elif y > 1:
                print(f'It will take {y} years and {z} months to repay the loan!')

        overpayment = (args.payment*periods - args.principal)
        print(f"Overpayment = {round(overpayment)}")

    elif args.payment is None:
        i = float((args.interest/100)/12)
        payment = (args.principal*i*math.pow(1+i, args.periods))/(math.pow(1+i, args.periods)-1)
        payment = math.ceil(payment)
        l_mon = args.principal - (payment*(args.periods-1))
        #if args.principal % args.periods == 0:
        print(f'Your monthly payment = {payment}')
        #else:
            #print(f'Your monthly payment = {payment} and the last payment = {l_mon}')

        overpayment = ((payment*args.periods) - args.principal)
        print(f'Overpayment = {round(overpayment)}')
