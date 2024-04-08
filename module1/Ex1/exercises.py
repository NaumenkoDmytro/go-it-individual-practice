from collections import defaultdict #we innitializing this to get an empty dictionaries wil already assign values for "keys" so we don't need to create a key evry time to assign a values into the dictionary
def groupAnagrams(strs: list[str]) -> list[str]:
    anagram_map = defaultdict(list) # we created a dictionary by using the defauldict to add new keys with values without creating a key each time for new values and the type for value will be list (by default)
    result = [] #an empty array that we will return as a result of function
    
    for s in strs: #here we are going trought each word in list
        sorted_s = tuple(sorted(s)) #the main idea here is to sort all elements in word in alphabtic oreder and assign it's copy as a key into our dictionary(anagram_map), we convert it into the tuple because list(mutable) data type can't be the key (always have to be immutable) in dictionaries
        anagram_map[sorted_s].append(s) #here we added they key to our (anagram map[sorted.s]), and add the word from the (strs) if it's match this key
    
    for values in anagram_map.values(): #will give us the list of the values
        result.append(values) #and for each of this values we are going to append them into our values list and return it

    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))