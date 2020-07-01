

anagram1 = 'bbbdddtttyyy'
anagram2 = 'yttdybbdtdby'

def isAnagram(anagram1, anagram2):

    return charMapping(anagram1) == charMapping(anagram2)

def charMapping(string):
    charMap = {}
    for char in string:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1

    return charMap

print(isAnagram(anagram1, anagram2))