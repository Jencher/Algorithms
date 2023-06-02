# User enters a string. Write a function to check if it is a palindrome or not.
# A string is said to be a palindrome if the reverse of the string is the same as string.
# For example, "radar" is a palindrome, but "radix" is not a palindrome.



string = input(f"Enter a string: ")

def palindrome_check(given_string):
    return given_string == given_string[::-1]

print(palindrome_check(string))




# Almost palindrome
def almost_palindrome(given_string):
    for i in range(len(given_string)):
        new_string = given_string[:i] + given_string[i+1:]
        if new_string == new_string[::-1]:
            return True
    return False

print(almost_palindrome('radix'))
print(almost_palindrome('radkar'))
print(almost_palindrome('radario'))