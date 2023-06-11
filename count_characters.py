# Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

str = input('Please enter a string: ')


def count_characters(str):
    vowels = 0
    consonants = 0
    for i in str:
        if i.isalpha():
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                vowels += 1
            else:
                consonants += 1

    return {
        'The number of vowels': vowels,
        'The number of consonants': consonants
    }

print(count_characters(str))