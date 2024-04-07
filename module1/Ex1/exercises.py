#Task: Write the Python program to remove duplicates from a list to also preserve the original order of elements in the list.

def remove_dublicates(elements:list) -> list:
    dup_items = set() #here we create a list for duplicates
    new_list = [] #here we create an empty list to store sorted data
    

    for elem in elements:
        if elem not in dup_items:
            new_list.append(elem)
            dup_items.add(elem)
        else:
            new_list.append(" ")
    return new_list

print(remove_dublicates([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))


