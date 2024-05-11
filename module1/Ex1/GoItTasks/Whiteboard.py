def longest_word(sentence: str) -> str:
    formated_text = sentence.split(' ')
    longest_word = ''
    print(formated_text)
    for word in formated_text:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word


#alterantive "clear"
def longest_word(sentence: str) -> str:
    return max(sentence.split(), key=len, default='')


#alterantive "creative"
def longest_word(sentence: str) -> str:
    sentence_sorted = sorted(sentence.split(' '), key=len, reverse=True)
    return sentence_sorted[0]


print("Example:")
print(longest_word("this is a sentence"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
