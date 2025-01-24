def average (numbers):
    return sum(numbers)/len(numbers)

def swap_values(a,b):
    temp = a
    a = b
    b = temp
    return a,b
def remove_duplicates(list1):
    return list(set(list1))
    
    

def average_main():
    numbers = []
    
    num = float(input("please enter the numbers that you want the average of "))
    num1 = float(input("please enter the numbers that you want the average of "))
    numbers.append(num)
    numbers.append(num1)
    print(average(numbers))
    
def swap_values_main():
    a = input("what value do you want to swap ")
    b = input("what number do you want to swap it with ")
    print(swap_values(a,b))

def remove_duplicates_main():
    list1 = []
    num = input("what value do you want to swap ")
    num1 = input("what number do you want to swap it with ")
    list1.append(num)
    list1.append(num1)
    print(remove_duplicates(list1))
    
    


remove_duplicates_main()