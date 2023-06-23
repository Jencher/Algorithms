# Your input is a list of integers, and you have to reorder its entries so that the even entries appear
# first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

array = [7, 3, 5, 6, 4, 10, 3, 2]

even = []
odd = []

for value in sorted(array):
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

combined = even + odd
print(combined)


# def even_odd(arr):
#     next_even = 0
#     next_odd = len(arr) - 1
#
#     print(f"Original: {arr}")
#
#     while next_even < next_odd:
#         if arr[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
#             next_odd -= 1
#
#     print(f"Result: {arr}")


test_list = [1, 4, 6, 3, 7, 9, 2, 22, 11]  # [4, 6, 2, 22, 1, 3, 7, 9, 11]
even_odd(test_list)