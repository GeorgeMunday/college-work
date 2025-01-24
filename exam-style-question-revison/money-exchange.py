def fees(money):
    if money > 300:
        money = money * 1.035
        print(f"this will cost you {money} with added fee")
        return money
    elif 300 < money < 750:
        money = money * 1.03
        print(f"this will cost you {money} with added fee")
        return money
    elif 750 < money < 1000:
        money = money * 1.025
        print(f"this will cost you {money} with added fee")
        return money
    elif 1000 < money < 2000:
        money = money * 1.02
        print(f"this will cost you {money} with added fee")
        return money
    else:
        money = money * 1.015
        print(f"this will cost you {money} with added fee")
        return money


def exchange_USD(money):
    money = money * 1.4
    money = round(money, 2)
    print(f"the new amount is {money} USD")


def exchange_EUR(money):
    money = money * 1.14
    money = round(money, 2)
    print(f"the new amount is {money} EUR")


def exchange_BLR(money):
    money = money * 4.77
    money = round(money, 2)
    print(f"the new amount is {money} BLR")


def exchange_JYP(money):
    money = money * 151.05
    money = round(money, 2)
    print(f"the new amount is {money} JYP")


def exchange_TRY(money):
    money = money * 5.68
    money = round(money, 2)
    print(f"the new amount is {money} TRY")


def main():
    print("the exchange rates are: \n1.USD = 1.4 \n2.EUR = 1.14 \n3.BLR = 4.77 \n4.JPY = 151.05 \n5.TRY = 5.68 ")

    options = {
        1: exchange_USD,
        2: exchange_EUR,
        3: exchange_BLR,
        4: exchange_JYP,
        5: exchange_TRY
    }

    question = input("are you a staff member")
    money = float(input("how much money would you like to transfer"))

    if question == "yes":
        money = money * 0.95

    money = fees(money)
    currency = input("what would you like to to transfer it to (use the numbers above eg 1,2,3,4,5)")
    options[int(currency)](money)


main()
