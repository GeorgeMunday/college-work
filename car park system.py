from datetime import datetime 
def carpark_logs():
    file = open("carparksystemlogs.txt", "r")
    filedat = file.read()
    print(filedat)
def Enter_carpark(car_plate):
    car_plate = input("what is your number plate charactors")
    with open("carparksystemlogs.txt", "a") as file:
        file.write(f"Car entered: {car_plate} at {now}\n")
        print("have a good day")

def Exit_carpark():
    car_plate = input("what is your number plate charactors")
    with open("carparksystemlogs.txt", "a") as file:
        file.write(f"exited: {car_plate} at {now}\n")
        print("have a good day")



now = datetime.now()  # Takes date and time from the system clock
car_name = ""
car_plate = ""
amount_max = 200
amount = 0  # Initialize the count of cars outside the loop

while True:
    print(f"There are {amount} cars in this car park.")
    choice1 = input("Would you like to 1.Enter or 2.Exit? ")

    # Validate input
    if not choice1.isnumeric():
        print("Invalid input. Please enter a number.")
        continue

    choice1 = int(choice1)

    if choice1 == 1:  # Enter
        if amount < amount_max:
            amount += 1
            print(amount)
            Enter_carpark(car_plate)
        else:
            print("The car park is full.")
            print(amount)
    elif choice1 == 2:  # Exit
        if amount > 0:
            amount -= 1
            Exit_carpark()
        else:
            print("The car park is already empty.")
            print(amount)
    elif choice1 == 3:
        code= int(input("this is for admins only\n enter the code\n *****"))
        if code == 12345:
            carpark_logs()
    else:
        print("Invalid choice. Please enter 1 to Enter or 2 to Exit.")