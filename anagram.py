# Anagram words have the same letters, for example 'heart' and 'earth' are anagram.
# Check if given string is an anagram of another string.



def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(is_anagram('abcd', 'aabcd'))
print(is_anagram('abcd1', 'dabc'))
print(is_anagram('abcd', 'dbca'))
print(is_anagram(' ', ' '))