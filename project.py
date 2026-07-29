from datetime import date
import sys
import re

budgets = ("Taxes: $3000.00\nRent: $1200.00\nInsurance: $100.00\
           \nUtilities: $200.00\nGroceries: $400.00\nEntertainment: $75.00\
           \nClothes: $90.00\nMiscellaneous: $125.00\
           \nInvestments: $2000.00")
def main():
    today = str(date.today())
    release = re.search(r"^[0-9]{4}-[0-9]{2}-01$", today)
    if release:
        monthly()
    if not release:
        with open("a.txt", "w") as f:
            f.write("1")
    try:
        if sys.argv[1] and sys.argv[2]:
            first = sys.argv[1]
            second = sys.argv[2]
            print(work(first, second, first) + "\n")
    except IndexError:
        print("No Change\n")
    print(originalbudget())

def monthly():
    with open("a.txt") as f:
        if f.read(1):
            with open("expenses.txt", "r") as f:
                for line in f:
                    negative = re.search(r"(\w+):\s*[$]-([\d.]+)", line)
                    if negative:
                        print(f"You went over your {negative.group(1)} budget by ${negative.group(2)} this month")
            file = open("expenses.txt", "w")
            file.write(budgets)

            with open("a.txt", "w") as f:
                f.write("2")

def work(type, money, first):
    try:
        works = False
        with open("expenses.txt") as fil:
            for line in fil:
                if ":" in line:
                    otype, omoney = line.strip().split(":")
                    if otype == type.capitalize():
                        works = True
                        orimoney = omoney.strip(" $")
                        break
        if works == True:
            toreplace = change(orimoney, money)
            if toreplace == "no":
                sys.exit()
        else:
            raise TypeError

        with open("expenses.txt") as fil:
                for line in fil:
                    if ":" in line:
                        otype, omoney = line.strip().split(":")
                    if otype == type.capitalize():
                        with open("expenses.txt") as fil:
                            expenses = fil.read()
                            expenses = expenses.replace(omoney, toreplace)
                        with open("expenses.txt", "w") as fil:
                                fil.write(expenses)
        with open("expenses.txt") as fil:
            return f"Changed {first}\n\n{fil.read()}"
    except TypeError:
        ret = "Typo! Try again."
        return ret


def change(orim, m):
    try:
        oridollars, oricents = orim.split(".")
        orivalue = int(oridollars + oricents)
        dollars, cents = m.split(".")
        value = int(dollars + cents)
        new = f"{(orivalue - value) / 100:.2f}"
        return str(" $" + new)
    except ValueError:
        print("Add two decimal places.")
        return "no"

def originalbudget():
    return "Original Budget:\n" + budgets

if __name__ == "__main__":
    main()
