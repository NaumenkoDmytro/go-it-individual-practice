#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    inverted_list = []
    for number in lst:
        if number > 0:
            inverted_list.append(-abs(number))
        elif number <= 0:
            inverted_list.append(abs(number))
    return inverted_list
   
        

        
   

    