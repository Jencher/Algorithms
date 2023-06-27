# Find and print max item and max index in a list

def find_max_item(arr):
    max_index = 0
    max_item = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_item:
            max_index = i
            max_item = arr[i]

    print(f"Max index: {max_index}, Max item: {max_item}")

test_list = [1, 4, 2, 87, 43, 4, 190, 8] # max_index = 6, max_item = 190
find_max_item(test_list)
