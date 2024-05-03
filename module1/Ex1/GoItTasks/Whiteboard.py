'''
Dict task with lambda: 6 
'''

def calculator(number1:int , number2:int , operator:str):
    operations = {'+': lambda x, y: x+y,
                  '-': lambda x, y: x-y,
                  '*': lambda x, y: x*y,
                  '/': lambda x, y: x/y}
    return operations[operator](number1,number2)

print(calculator(1,2,'+'))

        


