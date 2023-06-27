# Return the list, calculate the sum and multiplication of its elements
# Example: [1, 3, 7] Return[11, 21]

def sum_and_mult(arr):
    sum_result = 0
    mult_result = 1
    for number in arr:
        sum_result += number
        mult_result *= number

    print(f"Input list: {arr}")
    print(sum_result)
    print(mult_result)

test_list = [1, 3, 7]
sum_and_mult(test_list)
