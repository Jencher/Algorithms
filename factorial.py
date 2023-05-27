# 5! = 1*2*3*4*5 = 120


n = 5 #120
saved_n = n
result = 1

while n > 0:
    result = result * n
    n = n - 1

print(f'The factorial of {saved_n} = {result}')