num1 = int(124)
num2 = int(21)
num3 = int(32)

def max_of_three(number_1, number_2, number_3):
    max_item = number_1
    if max_item < number_2:
        max_item = number_2
    if max_item < number_3:
        max_item = number_3
    return max_item

# or return max([num1, num2,  num3])

print(max_of_three(num1, num2, num3))
