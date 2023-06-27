def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(arr)


list_to_sort = [4, 2, 6, 3, 1]
print(list_to_sort)
insertion_sort(list_to_sort)