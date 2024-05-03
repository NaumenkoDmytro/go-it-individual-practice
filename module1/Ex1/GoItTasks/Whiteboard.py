'''
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.

Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
'''

# Chat GPT attempt
import re

def CodelandUsernameValidation(strParam):
    # Define the pattern to match valid usernames
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{2,24}$')  # Username length: 4-25 characters

    # Check if the string length is within the valid range
    if len(strParam) < 4 or len(strParam) > 25:
        return False

    # Check if the string matches the pattern
    if not pattern.match(strParam):
        return False

    # Check if the username ends with an underscore
    if strParam.endswith('_'):
        return False

    return True

# That Works


#My attemp

# def CodelandUsernameValidation(strParam):
#         numbers = '1234567890'
#         underscores = '_'
#         pattern = re.compile(r'^[a-zA-Z0-9_]+$')
#         if len(strParam) < 4 or len(strParam) > 25:
#                 return False
#         elif strParam.startswith(numbers) or strParam.startswith(underscores):
#                 return False
#         elif pattern.match(strParam):
#                 return False
#         elif strParam.endswith(underscores):
#                 return False
#         else:
#                 return True


# keep this function call here 
print(CodelandUsernameValidation("u__hello_world123"))

