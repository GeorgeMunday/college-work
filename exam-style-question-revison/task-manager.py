tasks = {
    "task_list": [],
    "task_time": []
}

def add_tasks():
    choice = input("what task would you like to add").lower().strip()
    while True:
        try:
            task_time = int(input("Enter the time for the task: "))
            tasks["task_list"].append(choice)
            tasks["task_time"].append(task_time)
            break
        except ValueError:
            print("please enter a number")

def delete_task():
    choice = ("what task would you like to delete")

def view_tasks():
    print(tasks)


    
def access_granted():
    print("Welcome to task manager. What would you like to do?")
    options = {
        1: add_tasks,
        2: delete_task,
        3: view_tasks
    }
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 4:
                print("Exiting task manager.")
                break
            elif choice in options:
                options[choice]()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
