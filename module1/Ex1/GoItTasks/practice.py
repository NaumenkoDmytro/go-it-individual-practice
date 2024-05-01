'''
Taks 3: check if the string is in alphabtick oreder or not :)
'''

def is_alphabet(symbols:str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return  symbols.lower() in alphabet



print(is_alphabet("abc")) #isTrue
print(is_alphabet("aBc")) #isTrue
print(is_alphabet("abd")) #isFalse - після b йде c
print(is_alphabet("a")) #isTrue
print(is_alphabet("abcdefghjiklmnopqrstuvwxyz")) #isFalse - #j йде після i
print(is_alphabet("tuvwxyz")) #isTrue
print(is_alphabet("XYZ")) #isTrue


 # formated_str = symbols.lower()
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # if formated_str in alphabet:
    #     return True
    # else:
    #     return False