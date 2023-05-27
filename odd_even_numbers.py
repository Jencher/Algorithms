# count odd and even numbers. Count odd and even digits of the whole number.
#  E.g. if entered number 34560, then 3 digits will be even (4, 6, and 0) and 2 digits will be odd (3 and 5).

number = int(input(f"Enter a number"))

def count_odd_even(n):
    odd = 0
    even = 0
    for char in str(n):
        if int(char) % 2 == 0:
            even += 1
        else:
            odd += 1
    return {
        'odd': odd,
        'even': even
        }

print(count_odd_even(number))
