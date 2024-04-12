'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, 
but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
'''

def smash(words):
    if len(words) > 0:
        sentence =''
        for word in words:
            sentence += word
            sentence += ' '
    
        sentence = sentence.rstrip(sentence[-1])

        return sentence
    else:
        return ''


print(smash(['hello', 'world', 'this', 'is', 'great']))

#Alternative:

def smash(words):
    return " ".join(words)

#Done

'''
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!
'''

def better_than_average(class_points, your_points):
    #all_points = class_points.append(your_points) # I have no idea why that passed the test
    if (sum(class_points ) + your_points) /(len(class_points) + 1) > your_points:
        return False
    else:
        return True


#alternative

def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

print(better_than_average([2, 3], 5))

#Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        sum = 0
        for number in a:
            sum += number
    return sum
# Alternative
def sum_array(a):
  return sum(a)

#Done

#Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

def greet(name, owner):
    if name != owner:
        return 'Hello guest'
    else:
        return 'Hello Boss'

# Alternative

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

    
#Done


#Write a function to split a string and convert it into an array of words.

def string_to_array(s):
    return  s.split() if len(s) != 0 else ['']

# Alternative

def string_to_array(string):
    return string.split(" ")

#Done

#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
def invert(lst):
    inverted_list = []
    for number in lst:
        if number > 0:
            inverted_list.append(-abs(number))
        elif number <= 0:
            inverted_list.append(abs(number))
    return inverted_list

# Alternative
def invert(lst):
    return [-x for x in lst] # I have no idea why does it work

#Done