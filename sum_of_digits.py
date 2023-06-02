# n = 5 #15

def sum_of_digits(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

# or result = (n * (n+1))/2

print(sum_of_digits(5))

