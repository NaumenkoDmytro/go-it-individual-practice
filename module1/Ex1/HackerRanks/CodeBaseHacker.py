'''
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

'''

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    
#alternative

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2)) #eval functions here analyze the string and make the statement happen correct and return "int"
    
#Done

'''
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

'''
def find_average(array):
    if len(array) == 0:
        return 0
    else:
        return sum(array) / len(array)
        
    
# alternative with try and except:
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0
#done