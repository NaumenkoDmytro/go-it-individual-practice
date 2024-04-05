def add_function(numbers_to_add : list):
    total_add_sum = 0
    for num in numbers_to_add:
        total_add_sum +=num

    return total_add_sum

def multiplication_function(numbers_to_multi : list):
    total_multi_sum = 1 #always should be 1 becaouse it's multiplication
    for num in numbers_to_multi:
        total_multi_sum *= num
    return total_multi_sum

print(add_function([1,2,3]))
print(multiplication_function([1,2,2,3]))



