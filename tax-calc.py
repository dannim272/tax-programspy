
def uk_tax(income):
    calc = True
    while calc:
        if income > 125140:
            tax = (income - 125140)*.45
            tax = tax + (125140 - 50270)*.4
            tax = tax + (50270 - 12570)*.2
            calc = False
        if income > 50270:
            tax = tax + (income - 50270)*.4
            tax = tax + (50270 - 12570)*.2
            calc = False
        if income > 12570:
            tax = (income - 12570)*.2
            calc = False
    print("TAXES DUE: £",tax)


def fr_tax(income):
    calc = True
    while calc:
        if income > 168994:
            tax = (income - 168994)*.45
            tax = tax + (168994 - 78570)*.41
            tax = tax + (78570 - 27478)*.3
            tax = tax + (27478 - 10777)*.11
            calc = False
        if income > 78570:
            tax = (income - 78570)*.41
            tax = tax + (78570 - 27478)*.3
            tax = tax + (27478 - 10777)*.11
            calc = False
        if income > 27478:
            tax = (income - 27478)*.3
            tax = tax + (27478 - 10777)*.11
            calc = False
        if income > 10777:
            tax = (income - 10777)*.11
            calc = False
    print("TAXES DUE: €",tax)

def usa_tax(income):
    calc = True
    while calc:
        if income > 578126:
            tax = (income - 578126)*.37
            tax = tax + (578126 - 231251)*35
            tax = tax + (231251 - 182101)*.32
            tax = tax + (182101 - 95376)*.24
            tax = tax + (95376 - 44726)*.22
            tax = tax + (44726 - 11001)*.12
            tax = tax + 1100
            calc = False
        if income > 231251:
            tax = (income - 231251)*.35
            tax = tax + (231251 - 182101)*.32
            tax = tax + (182101 - 95376)*.24
            tax = tax + (95376 - 44726)*.22
            tax = tax + (44726 - 11001)*.12
            tax = tax + 1100
            calc = False
        if income > 182101:
            tax = (income - 182101)*.32
            tax = tax + (182101 - 95376)*.24
            tax = tax + (95376 - 44726)*.22
            tax = tax + (44726 - 11001)*.12
            tax = tax + 1100
            calc = False
        if income > 95376:
            tax = (income - 95376)*.24
            tax = tax + (95376 - 44726)*.22
            tax = tax + (44726 - 11001)*.12
            tax = tax + 1100
            calc = False
        if income > 44726:
            tax = (income - 44726)*.22
            tax = tax + (44726 - 11001)*.12
            tax = tax + 1100
            calc = False
        if income > 11001:
            tax = (income - 11001)*.12
            tax = tax + 1100
            calc = False
        if income < 11001:
            tax = income * .1
            calc = False
        print("TAXES DUE: $",tax)

print("ENTER COUNTRY FOR TAX CALCULATIONS FROM THE FOLLOWING LIST - UK[uk], France[fr], USA[usa]")
user_country = input()

if user_country == "uk":
    income = int(input("ENTER YOUR INCOME: "))
    uk_tax(income)

if user_country == "fr":
    income = int(input("ENTER YOUR INCOME: "))
    fr_tax(income)

if user_country == "usa":
    income = int(input("ENTER YOUR INCOME: "))
    usa_tax(income)
