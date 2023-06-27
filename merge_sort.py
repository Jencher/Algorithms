def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_arrays = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_arrays.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_arrays.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_arrays.append(left_arr[i])
            i += 1
        else:
            merged_arrays.append(right_arr[j])
            j += 1

    return merged_arrays

# print(merge_arrays([1, 5], [2, 7]))
list_to_sort = [4, 3, 2, 6, 9, 1]
print(list_to_sort)
print(merge_sort(list_to_sort))