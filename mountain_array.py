# Given an array of integers, return True if the following conditions are fulfilled:
# - length of the array is bigger than or equal to 3
# - there exists some index i such that:
# a[0]<a[1]< ...<a[i]
# a[i]>a[i+1]>...>a[a.size-1]

# To find if there is increasing trend following by decreasing trend

# [3, 5, 5] false
# [3, 4, 5, 2] true
# [5, 4, 7, 2] false


def is_mountain(arr):
    if len(arr) < 3:
        return False

    i = 1
    while i < len(arr) and arr[i] > arr[i-1]:
        i = i + 1
    if i == len(arr):
        return False
    while i < len(arr) and arr[i] < arr[i-1]:
        i = i + 1
    return i == len(arr)

arr1 = [3, 4, 5, 2]
arr2 = [3, 5, 5]
arr3 = [5, 4, 7, 2]
print(is_mountain(arr1))
print(is_mountain(arr2))
print(is_mountain(arr3))