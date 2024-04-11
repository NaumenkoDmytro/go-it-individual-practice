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
