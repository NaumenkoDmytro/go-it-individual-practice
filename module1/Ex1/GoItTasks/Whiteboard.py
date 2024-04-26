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