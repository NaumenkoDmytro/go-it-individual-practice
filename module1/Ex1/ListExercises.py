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
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
        return factorial(n) // ((factorial(n-k)) * factorial(k))
    
    
    
    