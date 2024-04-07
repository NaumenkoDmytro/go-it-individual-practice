#Task: Write a Python program to find the longest word in a given list of words.

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