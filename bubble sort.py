import random
import time

def bubble_main():
    def bubble_sort(numbers):
        # Get the length of the list
        length = len(numbers)
        count = 0
        # Go through the list multiple times
        for i in range(length):
            # Assume the list is sorted
            swapped = False
            
            # Compare adjacent numbers
            for j in range(length - 1):
                # If the current number is bigger than the next one, swap them
                if numbers[j] > numbers[j + 1]:
                    # Swap the numbers
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    swapped = True
            # If no numbers were swapped, the list is sorted, so stop early
            if not swapped:
                
                break

        return numbers

    # Example usage:
    unsorted_list =(random.sample(range(1, 100000), 10000))
    print("start")

    start_time = time.time()