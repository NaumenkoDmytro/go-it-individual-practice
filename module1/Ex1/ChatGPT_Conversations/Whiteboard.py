def sum_of_list_with_hash_table(lst):
    sum_table = {}
    for num in lst:
        if num in sum_table:
            sum_table[num] += num
            print(sum_table)
        else:
            sum_table[num] = num
            # print(sum_table)
    total_sum = sum(sum_table.values())
    return total_sum

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Sum of list using hash table:", sum_of_list_with_hash_table(my_list))