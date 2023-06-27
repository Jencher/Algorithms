# Find a sum of elements between min and max elements.
# Min and max elements are not included.
# All numbers are unique.

def sum_between_max_and_min(arr):
    if len(arr) <=2:
        return 0

    min_index = max_index = i = 0
    min_item = max_item = arr[0]

    while i < len(arr):
        if arr[i] > max_item:
            max_index = i
            max_item = arr[i]
        if arr[i] < min_item:
            min_index = i
            min_item = arr[i]
        i += 1
    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


test_list1 = [1, 4, 7, 23, 2]  # min = 1, max = 23
test_result1 = sum_between_max_and_min(test_list1)
print(test_result1)

test_list2 = [19, 4, 7, 3, 2]  # min = 2, max = 19
test_result2 = sum_between_max_and_min(test_list2)
print(test_result2)