def main(totalSales):
    while True:
        choice1 = input("What would you like to do\n1. Calculate commissions\n2. Calculate whole company sales\n3. Exit\n")

        if choice1 == "1":
            sales_amount = commission_user_acceptance()
            totalSales += sales_amount
        elif choice1 == "2":
            print(f"Total sales amount: {totalSales}")
        elif choice1 == "3":
            return totalSales
        else:
            print("Invalid choice. Please try again.")


def commissions_calculation(commission_rate, sales_amount):
    return commission_rate * sales_amount


def commission_user_acceptance():
    commission_rate = 500

    sales_am = int(input("How many sales did you make: "))
    commission = commissions_calculation(commission_rate, sales_am)

    print(f"Your commission is {commission}")
    return sales_am


def authenticate_user():
    valid_surname = ["surnameA", "surnameB", "surnameC"]
    valid_ID = ["123", "456", "789"]

    totalSales = 0
    attempt_count = 0

    while attempt_count < 3:
        entered_surname = input("What is your surname: ")
        entered_ID = input("What is your employee ID: ")
        attempt_count += 1

        if entered_surname in valid_surname and entered_ID in valid_ID and valid_surname.index(entered_surname) == valid_ID.index(entered_ID):
            main(totalSales)
            attempt_count = 0

        else:
            print("Invalid username or password")

    if attempt_count >= 3:
        print("Contact admin")


authenticate_user()
