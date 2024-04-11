'''
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

'''
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2)) #eval functions here analyze the string and make the statement happen correct and return "int"

print(type(basic_op('+', 4, 7)))
