# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

string1 = input(f"Enter a string: ")


def isUniqueChars(string):
    result = ''
    for char in string:
        if char not in result:
           result += char
    if result == string1:
        return True
    else:
        return False

print(isUniqueChars(string1))