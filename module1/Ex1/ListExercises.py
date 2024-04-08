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
    for_smallest_number = numbers[0] #Here we assign the integer type of data
    for num in numbers: #Num here is also an integer, so can work with two integers
            if num < for_smallest_number: # if large number needed change the < sign to
                for_smallest_number = num #assign one integer to another
    return for_smallest_number #and here we return integer

print(min_number_in_list([1,1111,2443,45,65,76,67]))

#Done
#5. Створіть програму на Python, яка розраховує суму всіх цілих чисел від 1 до числа, введеного користувачем.
num = int(input("Enter the integer (0 to 100): "))
sum = 0
while num > 0:
   sum +=num
   num -= 1 

#Done

#5. Напишіть функцію get_fullname на Python, яка приймає ім'я, прізвище та, опціонально, друге ім'я (або по батькові) та повертає рядок з повним іменем користувача.

def get_fullname(first_name, last_name, middle_name =""  ):
    if len(middle_name) == 0:
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}"
    
#Done

#6. Напишіть функцію format_string, яка центрує рядок у рамках заданої довжини length.
'''
Задачі:
1) Створіть функцію format_string, яка приймає два аргументи: string рядок, який потрібно форматувати та length довжина, у межах якої потрібно центрувати рядок.
2) Якщо довжина string більша або дорівнює length, поверніть рядок без змін.
3) Якщо довжина string менша за length, додайте перед рядком пробіли, для того, щоб рядок був центрований у рамках length.
'''
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces_count = (length - len(string)) // 2
        return f"{' ' * spaces_count}{string}"
#Done

'''
Наступне завдання буде суто теоретичним, і ми потренуємося створювати функції в Python, які можуть приймати довільну кількість позиційних або ключових аргументів.

Задачі:

Створіть функцію first, яка приймає один обов'язковий аргумент size та довільну кількість позиційних аргументів. Функція має повертати суму: size + кількість позиційних аргументів.
Створіть функцію second, яка також приймає один обов'язковий аргумент size та довільну кількість ключових аргументів. Функція має повертати суму: size + кількість ключових аргументів.
В обох функціях використовуйте спеціальні синтаксиси * для позиційних аргументів та ** для ключових аргументів.
Очікуваний результат:

Функції повинні коректно розраховувати суму size та кількості переданих аргументів.
'''
def first(size, *args):
    ar = len(args)
    total_sum_ar = size + ar
    
    return total_sum_ar


def second(size,**kwargs ):
    kw = len(kwargs)
    total_sum_kw = size + kw
    
    return total_sum_kw

# Done

'''
Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)

де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k, і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

Задачі:

1.Створіть функцію number_of_groups, яка приймає два аргументи: n - загальна кількість людей та k - кількість переможців.
2.У функції number_of_groups, використовуйте функцію factorial для обчислення факторіалів відповідно до формули сполучень: Cnk = n! / ((n - k)! · k!).
3.Обчислення здійснюється шляхом виклику функції factorial для отримання факторіалів n, n - k та k.
4.Поверніть результат цього обчислення.
'''
def factorial(n): #функція яка виконує обчислення факторіалу
    if n < 2: # умова зупинки виклику функції
        return 1
    else:
        return n * factorial(n - 1) # обчислення факторілу


def number_of_groups(n, k):
        return factorial(n) // ((factorial(n-k)) * factorial(k)) #використання рекурсивної функції факторіалу
    
    
# Done
# Task: Write a Python program to find the maximum value in a list.
def finding_max_in_list(items:list) -> int:
    max_number = 0
    for item in items:
        if item > max_number:
            max_number = item
    return max_number


print(finding_max_in_list([1,2,3,4,5,6,7,1000]))

# Done

#Task: Write a Python program to find the average length of strings in a given list of strings.
def average_rage_of_string(words:list) -> float: #assign the types of arguments and expected reults
    total_string_lenght = 0 # assign the variable to count the total lenght of string in list
    for elem in words:
        total_string_lenght += len(elem) #counting the total lenght of strings
    
    return total_string_lenght / len(words) # return the average of all elemnts in list of strings


print(average_rage_of_string(['radar', 'level', 'python', 'noon', 'pop']))
# Done

#Task: Write a Python program to find the longest word in a given list of words.

def the_longest_word(words:list) -> str: #define the types of data that function have to accept
    longest_word = '' #create an empty str to assing value from loop
    for elem in words:
        if len(elem) > len(longest_word): #check if lenght of the previous elemt  bigger then our empty string (here I had to be carful with data type for check "int" should check with "int")
            longest_word = elem #if True assign str value to our empty string
    return longest_word #return the biggest string form the list

print(the_longest_word(['radar', 'level', 'python', 'noon', 'pop','jfkdskhjgfjkdfgjgfdjgfdklfgdlkgfdlkgfdklgfdkl']))

# Done

#Task: Write a Python program to find the longest word in a given list of words. (I added a check for other data types in this function, so now it works only with strings :) )

def the_longest_word(words:list) -> str:
    longest_word = '' 
    for elem in words:
        if isinstance(elem, str):
            if len(elem) > len(longest_word):
                longest_word = elem
        else:
            print(f" {elem} is't a string, sorry but we work only with strings :)")
    return longest_word

print(the_longest_word([123456,'radar', 'level', 'python', 'noon', 'pop','jfkdskhjgfjkdfgjgfdjgfdklfgdlkgfdlkgfdklgfdkl']))

# Done

#Task: Write a Python program to find the median of a given list of numbers.

def find_median(numbers):
    numbers.sort()  # Sort the list of numbers
    n = len(numbers)
    if n % 2 == 1:
        # If the length of the list is odd
        return numbers[n // 2]
    else:
        # If the length of the list is even
        mid1 = n // 2
        mid2 = mid1 - 1
        return (numbers[mid1] + numbers[mid2]) / 2

# Example usage
my_numbers = [5, 3, 1, 4, 2]
print("Median of the list:", find_median(my_numbers))

#analyzed

# Define a list 'a' with some duplicate and unique elements
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Create an empty set to store duplicate items and an empty list for unique items
dup_items = set()
uniq_items = []

# Iterate through each element 'x' in the list 'a'
for x in a:
    # Check if the current element 'x' is not already in the set 'dup_items' (it's a duplicate check)
    if x not in dup_items:
        # If 'x' is not a duplicate, add it to the 'uniq_items' list
        uniq_items.append(x)
        # Add 'x' to the 'dup_items' set to mark it as a seen item
        dup_items.add(x)

# Print the set 'dup_items' which now contains the unique elements from the original list 'a'
print(dup_items) 

#analyzed

# Task: Implement a function that checks if two lists have the same elements in the same order and return True if they do, otherwise return False.
a = [1,2,3]
def same_elemts_check(elements_set_first: list, elements_set_second: list ) -> bool:
    if elements_set_first is elements_set_second:
        return True
    else:
        return False

print(same_elemts_check(a, a))
print(same_elemts_check(a, [1,2,3]))

#Done

#Task: Write the Python program to remove duplicates from a list to also preserve the original order of elements in the list.

def remove_dublicates(elements:list) -> list:
    dup_items = set() #here we create a set for duplicates
    new_list = [] #here we create an empty list to store sorted data
    

    for elem in elements:
        if elem not in dup_items:
            new_list.append(elem)
            dup_items.add(elem)
        else:
            new_list.append(" ")
    return new_list

print(remove_dublicates([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))

#Done

#Task: Given an array of string (strs), group the anagrams together. (hash-map)
from collections import defaultdict #we innitializing this to get an empty dictionaries wil already assign values for "keys" so we don't need to create a key evry time to assign a values into the dictionary
def groupAnagrams(strs: list[str]) -> list[str]:
    anagram_map = defaultdict(list) # we created a dictionary by using the defauldict to add new keys with values without creating a key each time for new values and the type for value will be list (by default)
    result = [] #an empty array that we will return as a result of function
    
    for s in strs: #here we are going trought each word in list
        sorted_s = tuple(sorted(s)) #the main idea here is to sort all elements in word in alphabtic oreder and assign it's copy as a key into our dictionary(anagram_map), we convert it into the tuple because list(mutable) data type can't be the key (always have to be immutable) in dictionaries
        anagram_map[sorted_s].append(s) #here we added they key to our (anagram map[sorted.s]), and add the word from the (strs) if it's match this key
    
    for values in anagram_map.values(): #will give us the list of the values
        result.append(values) #and for each of this values we are going to append them into our values list and return it

    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#analyzed, done with youtube.
