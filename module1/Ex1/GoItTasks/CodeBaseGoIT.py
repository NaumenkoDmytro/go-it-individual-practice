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


#Taks: Write a Python program that takes a list of strings as input and prints each string along with its index in the list.

name_list = ['Alice','Bob','Charle','David','Emily']
for i, value in enumerate(name_list):
    print(f'Index is = {i}, value of this index = {value}')

#Done

#Write a Python function called combine_lists that takes two lists of equal length as input and returns a list of tuples where each tuple contains elements from corresponding indices of the input lists.
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
new_list = []
if len(list1) == len(list2):
    for number, value in zip(list1,list2):
        appendr =(number,value) 
        new_list.append(appendr)
else:
    print('lists have not equal lenght')

print(new_list)

#Done
#Перевірка балансу для здійснення покупки
balance = 0.7 + 0.6
print(balance)
if round(balance, 1) == 1.3: #always use round with float numbers
    print('Enough')
else:
    print('Not Enough')
print(round(balance, 1))

#analyzed
#У результаті виклику методу now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:
from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year) 
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

#analyzed
# Datetime for homework
from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2
#analyzed

#Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. Він відповідає за відрізок часу між двома датами.
from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0
print(type(difference))
print(type(seventh_day_2019))

#analyzed

#Вибір з вагами:
import random

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1] #задає weight для списку
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color) 

#analyzed

'''
Вимоги до завдання:

Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

'''

import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max < min or quantity <1 or quantity > 1000 or quantity > max-min+1:
        print(f"Out of range")
        return list()
    else: 
        ticket_list = set()
        while len(ticket_list) < quantity:
            ticket_list.add(random.randint(min, max))

        print(f"The range of number starts from: {min} to {max}")
        return ticket_list
          
        

lottery_numbers = get_numbers_ticket(1, 100, 9)
print("Ваші лотерейні числа:", lottery_numbers)
print(len(lottery_numbers))

#Done

import random
import time

start_time = time.perf_counter()

#Task #2
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max < min or quantity <1 or quantity > 1000 or quantity > max-min+1:
        print(f"Out of range")
        return list()
    # else:
    #     ticket_list = range(min, max+1)
    #     the_main_list = sorted(random.sample(ticket_list, quantity))
    #     #final_list = sorted(the_main_list)   
    # return the_main_list
    # Nice one option :)
    #return sorted(random.sample(range(min, max+1), quantity))
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
        
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")
    
#0.0001981999957934022 секунд > Час виконання: 0.00016469997353851795 секунд
#Done



# Autotest task 1
from datetime import datetime


def string_to_date(date_string):
    datetime_object = datetime.strptime(date_string, '%Y.%m.%d')
    return datetime_object
    
    
def date_to_string(date):
    string_object = date.strftime('%Y-%m-%d')
    return string_object

'''
Якщо функція string_to_date отримала рядок 2020.01.01 то вона повинно повернути обєкт datatime: 2020-01-01. Поточний результат: : time data '2020.01.01' does not match format '%Y-%m-%d'

'''

print(string_to_date('2020.01.01'))

#  У Харкові відкривають у бомбосховищі школу для молодших школярів.
# Треба  обладнати три кімнати партами. Парта  - на дві людини.
# Програмі подається на вхід три числа (трьома input)  - кількість учнів в кожному
# класі. Програма має порахувати необхідну кількість парт загалом.



# first_class_people = int(input('Введіть кількість учнів першому классі:'))
# second_class_people = int(input('Введіть кількість учнів другому лассі:'))
# third_class_people = int(input('Введіть кількість учнів третьому классі:'))


# first_class_tables = first_class_people // 2 + first_class_people % 2
# second_class_tables = second_class_people // 2 + second_class_people % 2 
# third_class_tables = third_class_people // 2 + third_class_people % 2

# print(f'В перший класс потрібно {first_class_tables} парт,В другий класс потрібно {second_class_tables} парт, В третій класс потрібно {third_class_tables} парт, всьго потрібно парт {first_class_tables + second_class_tables + third_class_tables }')

# Зчитайте дійсне число. Виведіть його першу цифру після крапки.

# number = ((89.12 % 1) * 10)
# print(int(number))

# Плюсами намалювати  такий трикутник
#   +
#   +++
#   +++++
#   +++++++
#   +++++++++

# for i in range(5):
#     i = "+" * 2
#     print(i)
# i = 5
# x = 1
# while i > 0:
#      print(' '*(i-1) + 'x'*(10-i*2+1))
#      i -= 1

#Done

# В рядку написан текст. 
# Для кожного слова підрахуйте 
# кілька разів воно зустрічалось в цьому тексті.

# text = '''
#         Little girl, little girl Why are you crying? Inside your restless soul your heart is dying Little one, little one Your soul is purging Of love and razor blades Your blood is surging Runaway From the river to the street And find yourself with your face in the gutter Your a stray for the salvation army There is no place like home When you got no place to go Little girl, little girl Your life is calling The charlatans and saints of your abandon Little one little one The sky is falling The lifeboat of deception is now sailing In the wake all the way No rhyme or reason Your bloodshot eyes Will show your heart of treason Little girl little girl You dirty liar You're just a junkie Preaching to the choir Runaway To your lost tranquility And find yourself with your face in the gutter Your a stray for the dregs of humanity There is no place like home When you got no place to go The traces of blood Always follow you home Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. Sister of grace. Runaway From the river to the street And find yourself with your face in the gutter You're a stray for the salvation army There is no place like home When you got no place to go
#         '''
# text = text.replace(',',' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').lower()
# word_counter = {}
# text_splt = text.split()
# for word in text_splt:
#     word_counter[word] = word_counter.get(word, 0) + 1
# # Перегорнули список    
# word_counter_reversed = {}
# for key, value in word_counter.items():
#     word_counter_reversed[value] = word_counter_reversed.get(value, []) + [key]
# # Вивели відсортований список
# sorted_words = sorted(word_counter_reversed)
# for word in sorted_words:
#     print(word,word_counter_reversed[word])

# #Done


# Нам треба написати код, який обробляє URL пошукового запиту, щоб видобути параметри запиту та перетворити їх у формат, з яким легше працювати в Python.
#Перший шаг ми відділяємо параметри запросу
url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)
# дадаємо словник з ключ значеннями і розділяємо його
obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

#Analyzed
# Autocheck #2 module 3
from datetime import datetime


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def prepare_user_list(user_data):
    for user in user_data:
        user["birthday"] = string_to_date(user["birthday"])
    return user_data

#done #analyzed