'''
Є якісь данні, як приклад 'AAAAABBbCCCCC' повернтуи массив унікальних значень без повторювань - [A,B,b,C]
'''

def solution(data) -> list:
    result = []
    last_element = None

    for element in data:
        if element != last_element:
            result.append(element)
            last_element = element

    return result

print(solution('AAAAABBbCCCCC'))
print(solution([1,1,1,2,3,4,5,5,5]))