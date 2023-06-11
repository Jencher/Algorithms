# When given a list of elements find the two lowest elements.
# They can be equal to each other or different
# Example: [196, 3, 4, 9, 10, 98, 2]    Answer: 2, 3

def find_elements(arr):
    arr.sort()
    return arr[0:2]

arr = [196, 3, 4, 9, 10, 98, 2]
print(find_elements(arr))
