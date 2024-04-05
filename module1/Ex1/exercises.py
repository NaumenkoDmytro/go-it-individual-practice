def min_number_in_list(numbers: list):
    for_smallest_number = numbers[0] #Here we assign the integer type of data
    for num in numbers: #Num here is also an integer, so can work with two integers
            if num < for_smallest_number: # if large number needed change the < sign to
                for_smallest_number = num #assign one integer to another
    return for_smallest_number #and here we return integer

print(type(min_number_in_list([1,1111,2443,45,65,76,67])))