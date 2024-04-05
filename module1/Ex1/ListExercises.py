#1. Write a Python program to sum all the items in a list.
def add_function(numbers_to_add : list):
    total_add_sum = 0
    for num in numbers_to_add:
        total_add_sum +=num

    return total_add_sum

print(add_function([1,2,3]))
#Done

#2. Write a Python program to multiply all the items in a list.
def multiplication_function(numbers_to_multi : list):
    total_multi_sum = 1 #always should be 1 becaouse it's multiplication
    for num in numbers_to_multi:
        total_multi_sum *= num
    return total_multi_sum


print(multiplication_function([1,2,2,3]))

#Done
#3. Write a Python program to get the largest number from a list.

def largest_number_function(numbers: list):
    maximum_number = max(numbers)
    return maximum_number

print(largest_number_function([1,1111,2443,45,65,76,67]))

#Done

#4. Write a Python program to get the smallest number from a list.

def min_number_in_list(numbers: list):
    for_smallest_number = numbers[0]
    for num in numbers:
            if num < for_smallest_number: # if large number needed change the < sign to > 
                for_smallest_number = num
    return for_smallest_number

print(min_number_in_list([1,1111,2443,45,65,76,67]))

