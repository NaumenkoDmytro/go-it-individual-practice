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

# Пригадаємо як звучить наше завдання. У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, 
# вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. 
# Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday #повертає обект datetime.date


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year+1)
        
        """
        Додайте на цьому місці перевірку, чи не буде 
        припадати день народження вже наступного року.
        """
           

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            
            """ 
            Додайте перенесення дати привітання на наступний робочий день,
            якщо день народження припадає на вихідний. 
            """
        
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays

#done # Saved for future projects


#Всі файли потрібно навмистно приводити до UTF - 8 такі правила...
# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
#Analyzed


'''
Дан рядок. 
Розріжте його навпіл і переставте ці половинки містами.
Якщо довжина непарна, то перша частина буде більшою.

'''


# line = '12345'
# line_middle = round(len(line)//2) + len(line)%2
# first_half = line[:line_middle]
# second_half = line[line_middle:]
# reversed_line =  second_half + first_half

# print(reversed_line)
   
   
   
'''
Дан рядок.
НАйдіть в ньому другу букву "а". Виведіть індекс.
Якщо є тільки одна  - виведить "alone", якщо взагалі нема
виведіть None
'''
# def find_second_occurrence(s, char):
#     first_occurrence = s.find(char)
#     if first_occurrence == -1:
#         return None
#     second_occurrence = s.find(char, first_occurrence + 1)
#     return second_occurrence


# index_of_second_a = find_second_occurrence("banaaana", "a")
# print(index_of_second_a)
'''
У Джо Палуки товсті пальці, тому він завжди натискає клавішу "Caps Lock", коли насправді має намір натиснути клавішу "a". 
(Коли Джо намагається ввести якусь акцентовану версію "a", яка потребує більше натискань клавіш для створення акцентів, 
він більш обережний у присутності таких рафінованих символів ([Shift] + [a]) і буде натискати клавіші правильно). 
Обчисліть і виведіть результат введення Джо заданого тексту. 
Клавіша "Caps Lock" впливає лише на клавіші з літерами від "a" до "z", і не впливає на інші клавіші або символи. вважається, що клавіша "Caps Lock" спочатку вимкнена.
assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
'''  

# def caps_lock(text):
#     formated_text = text.split('a')
#     for i in range(1, len(formated_text),2):
#         formated_text[i] = formated_text[i].upper()
#     print(''.join(formated_text))
#     return ''.join(formated_text)

    



# assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
# assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
# assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

'''
Як із рядка слов отримати словник де ключи та значення записані попарно.
Наприклад: "Hello Hi Bye Goodbye List Array"
{"Hello": "Hi", 
"Bye": "Goodbye", 
"List": "Array"}
'''
'''
У тебе є таблиця з усіма наявними товарами в магазині. Дані представлені у вигляді списку словників

Твоя місія - знайти ТОП найдорожчих товарів. Кількість товарів, які ми шукаємо, буде передано у першому аргументі, а самі дані щодо товарів будуть передані другим аргументом.

Вхідні дані: Число та список словників (int and list of dicts). Кожен словник має 2 ключі "name" та "price".

Вихідні дані: Такий, як і другий аргумент.

Приклади:

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]
'''
# def sort_price(dict_:dict):
#     return -dict_['price'] #check tommorow

# def bigger_price(count:int , goods:list):
#     print(sorted(goods, key=sort_price)[:count])
#     return sorted(goods, key=sort_price)[:count]



# assert bigger_price(
#     2,
#     [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1},
#     ],
# ) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
# assert bigger_price(
#     1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
# ) == [{"name": "whiteboard", "price": 170}]

'''
Тобі дано словник із акціями і їх цінами. Функція повинна повертати найдорожчу акцію.

Вхідні значення: Словник, у якому біржовий тікер (коротка назва) акції є ключем, а значенням є ціна цієї акції.

Вихідні значення: Біржовий тікер як рядок.

Приклади:

assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

Передумови: Ціни є унікальними, тобто не повторюються.
'''


# def best_stock(stock):
#     print(sorted(stock, key=stock.get))
#     return sorted(stock, key=stock.get)[-1]
    

# assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
# assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

'''
Coin Change Problem
You are given an unlimited supply of coins of certain denominations and a total amount of money. 
Write a function that returns the number of distinct ways you can make the total amount using these coins. 
The order of coins does not matter.

Input:

coins: a list of integers representing the coin denominations available.
amount: an integer representing the total amount of money.
Output:

Return the number of ways you can make the amount using any number of coins from coins.
'''

# def count_ways(coins, amount):
#     cache = {}
#     def recursive_count(current_amount):
#         if current_amount in cache:
#             return cache[current_amount]
#         elif current_amount == 0:
#             return 1
#         elif current_amount < 0:
#             return 0 
    
#         result = 0
#         for coin in coins:
#             result += recursive_count(current_amount - coin)

#         cache[current_amount] = result
#         return result
#     return recursive_count(amount)
    
# coins = [1, 3, 4]
# amount = 10
# print(count_ways(coins, amount))
"""
Ми створимо клас Pokemon, що ілюструє основні принципи об'єктно-орієнтованого програмування (ООП), а потім створимо об'єкт класу Pokemon - pikachu. 
Клас Pokemon буде містити атрибути: name, type, і health.

Для класу ми визначимо наступні методи:

attack (напад) - дозволяє покемону атакувати іншого покемона.
dodge (уклон) - дає можливість уникнути атаки.
evolve (еволюціонувати) - дозволяє покемону еволюціонувати в іншу форму.
"""
class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


'''
Taks polindrome problem: context - is a word a polindrome?
'''

# def is_palindrome(word: str) -> bool:
#     return word.lower() == word[::-1].lower()
    


# print(is_palindrome('radar'))  # True
# print(is_palindrome('hello'))  # False
# print(is_palindrome('level'))  # True
# print(is_palindrome('Level'))  # True


# # formated_word = word.lower()
# #     new_word = ''
# #     for i in formated_word[::-1]:
# #         new_word += i
# #     if new_word == formated_word:
# #         return True
# #     else:
# #         return False


'''
Booking a hotel room: context : find out if the number is available for booking.
'''

# def calculate_guests(request: str) -> int or str:
#     number_of_guests = ''
#     for char in request:
#         print(char)
#         if char.isnumeric():
#             number_of_guests += char
#         elif len(number_of_guests) != 0:
#             break 
        
#     print(number_of_guests)     
#     return 'not a number' if number_of_guests == '' or number_of_guests == '0' else int(number_of_guests)
 


# print(calculate_guests("I think 5 guests") == 5)
# print(calculate_guests("Big company of 15 dudes") == 15)
# print(calculate_guests("5") == 5)
# print(calculate_guests("alone") == "not a number")
# print(calculate_guests("0") == "not a number")
# print(calculate_guests("Hello, 9.75 people") == 9)
# print(calculate_guests("There will be 7 or 9 guys") == 7)
# print(calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk") == 12)

'''
Taks 3: check if the string is in alphabtick oreder or not :)
'''

# def is_alphabet(symbols:str) -> bool:
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return  symbols.lower() in alphabet



# print(is_alphabet("abc")) #isTrue
# print(is_alphabet("aBc")) #isTrue
# print(is_alphabet("abd")) #isFalse - після b йде c
# print(is_alphabet("a")) #isTrue
# print(is_alphabet("abcdefghjiklmnopqrstuvwxyz")) #isFalse - #j йде після i
# print(is_alphabet("tuvwxyz")) #isTrue
# print(is_alphabet("XYZ")) #isTrue


 # formated_str = symbols.lower()
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # if formated_str in alphabet:
    #     return True
    # else:
    #     return False

'''
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.

Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
'''

# Chat GPT attempt
import re

def CodelandUsernameValidation(strParam):
    # Define the pattern to match valid usernames
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{2,24}$')  # Username length: 4-25 characters

    # Check if the string length is within the valid range
    if len(strParam) < 4 or len(strParam) > 25:
        return False

    # Check if the string matches the pattern
    if not pattern.match(strParam):
        return False

    # Check if the username ends with an underscore
    if strParam.endswith('_'):
        return False

    return True

# That Works


#My attemp

# def CodelandUsernameValidation(strParam):
#         numbers = '1234567890'
#         underscores = '_'
#         pattern = re.compile(r'^[a-zA-Z0-9_]+$')
#         if len(strParam) < 4 or len(strParam) > 25:
#                 return False
#         elif strParam.startswith(numbers) or strParam.startswith(underscores):
#                 return False
#         elif pattern.match(strParam):
#                 return False
#         elif strParam.endswith(underscores):
#                 return False
#         else:
#                 return True


# keep this function call here 
print(CodelandUsernameValidation("u__hello_world123"))

'''
Dict task: 1
'''

def user_update(user_data:list) -> None:
    for user in user_data:
        user['full_name'] = user['first_name'] +' '+ user['last_name']
        print(user['full_name'])
    



users = [
  {
    "first_name": "Jack",
    "last_name": "Holy",
  },
  {
    "first_name": "Mike",
    "last_name": "Adams",
  },
]

print(user_update(users))
print(users)

'''
Dict task: 2 
'''

def user_update(user_data:list) -> None:
    for user in user_data:
        user['first_name'] = user['full_name'].split(' ')[0]
        

users = [
        { 'last_name': 'Holy', 'full_name': 'Jack Holy'}, 
         { 'last_name': 'Adams', 'full_name': 'Mike Adams'},
         { 'last_name': 'Adams', 'full_name': 'Mikessss Adams'}
        ]

print(user_update(users))
print(users)

'''
Dict task: 3 
'''

def user_update(user_data:list) -> None:
    for user in user_data:
        if user["status"] == "disabled":
            user.pop("country")

        

users = [
  { "name": "Emma", "status": "active", "country": "Ukraine" },
  { "name": "Avram", "status": "disabled", "country": "Poland" },
  { "name": "Avram", "status": "active", "country": "Poland" },
  { "name": "Avram", "status": "disabled", "country": "Poland" },
]

print(user_update(users))
print(users)

'''
Dict task: 4 
'''

def robot_version_check(robot_data:list, version:int) -> None:
    index_list =[i for i, item in enumerate(robot_data) if item["core_version"] < version]
    # for i, item in enumerate(robot_data):
    #     if item["core_version"] < version:
    #         index_list.append(i)
    return index_list
            

robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

print(robot_version_check(robots, 10))  #[0, 3])
print(robot_version_check(robots, 14))  #[0, 1, 3])
print(robot_version_check(robots, 8))  #[])
print(robot_version_check(robots, 18))  #[0, 1, 2, 3, 4])

'''
Dict task with lambda: 5 
'''

def calculator(number1:int , number2:int , operator:str):
    operations = {'+': lambda x, y: x+y,
                  '-': lambda x, y: x-y,
                  '*': lambda x, y: x*y,
                  '/': lambda x, y: x/y}
    return operations[operator](number1,number2)

print(calculator(1,2,'+'))