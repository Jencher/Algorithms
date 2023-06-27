# Remove all duplicates from a sorted list and the remaining elements has been shifted left to fill the
# emptied indices.
# Fill the remaining indices with zeroes.
# return the number of valid elements.

# [1, 1, 2, 2, 3, 4, 5, 5] -> [1, 2, 3, 4, 5, 0, 0, 0] -> 5 elements

def delete_duplicates(arr):
    write_index = 1

    print(f"Input list: {arr}")
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    print(f"Result list: {arr}")
    return write_index

test_list = [1, 1, 1, 2, 2, 3, 4, 5, 5]
result = delete_duplicates(test_list)
print(f"Number of valid elements: {result}")


