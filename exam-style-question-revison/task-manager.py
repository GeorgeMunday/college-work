def add_delete_tasks():
    choice = input("Would you like to add or delete a task?")

def view_tasks():
    choice = input("")

def access_granted():
    print("Welcome to task manager. What would you like to do?")
    options = {
        1: add_delete_tasks,
        2: "Delete Task",
        3: view_tasks
    }

def main():
    usernames = ["user1", "user2", "user3"]
    passwords = ["pass1", "pass2", "pass3"]
    count = 0
    choice = ""
    choice1 = ""

    while True:
        while count < 3:
            username = input("Username: ")
            password = input("Password: ")
            if username in usernames and password in passwords and usernames.index(username) == passwords.index(password):
                print("Access granted")
                access_granted()
                continue
            else:
                print("Username or password incorrect")
                count += 1

        choice = input("Have you forgotten your password? ").lower().strip()
        if choice == "yes":
            choice1 = input("What is your username? ")
            if choice1 in usernames:
                new_password = input("Enter new password: ")
                index = usernames.index(choice1)
                passwords[index] = new_password
                print("Password changed successfully")
                count = 0
                continue
            else:
                print("Username not found")
                break
        else:
            print("Stopping program")
            break

if __name__ == "__main__":
    main()
