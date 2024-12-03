import random 
import time  # Import the time module to track execution time 
def binary_search(list2, search_value): 
    list_start = 0 
    list_end = len(list2) - 1 
    while list_start <= list_end: 
        mid = (list_start + list_end) // 2  # Correct middle index calculation 
        if list2[mid] == search_value:  # Compare the value at mid to search_value 
            return True  # Found the value 
        elif list2[mid] < search_value: 
            list_start = mid + 1  # Search the right half 
        else: 
            list_end = mid - 1  # Search the left half 
    return False  # Value not found 
def main(): 
    # Generate a sorted list of 10 unique numbers between 1 and 19 
    list2 = sorted(random.sample(range(1, 20), 10)) 
    print("Welcome to Binary Search!") 
    print(f"Here is the list: {list2}")  # Display the list 
    while True: 
        # User input for the value to search 
        while True: 
            search_value = input("Enter a value to search: ") 
            if search_value.isnumeric(): 
                search_value = int(search_value) 
                print(f"You entered the number {search_value}") 
                break  # Exit the inner loop if input is valid 
            else: 
                print("You did not enter a valid number. Please try again.") 
        # Record the start time of the binary search 
        start_time = time.time() 
        # Perform binary search 
        if binary_search(list2, search_value): 
            print(f"{search_value} was found in the list!") 
        else: 
            print(f"{search_value} is not in the list.") 
        # Record the end time after the binary search 
        end_time = time.time() 
        # Calculate the elapsed time 
        elapsed_time = end_time - start_time 
        print(f"Binary search took {elapsed_time:.17f} seconds.") 
        # Ask if the user wants to perform another search 
        another_search = input("Would you like to search again? (yes/no): ").strip().lower() 
        if another_search != "yes": 
            print("Thank you for using the Binary Search Program!") 
            break  # Exit the loop and end the program 
# Run the program 

main() 

 
 

 

 
 