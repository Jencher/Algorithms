# Find which element is missing in second list

my_list1 = [1, 6, 10, 7, 2, 11]
my_list2 = [6, 1, 2, 7, 11]

def missing_element(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for i in range(len(arr2)):
        if arr1[i] != arr2[i]:
            return arr1[i]
    return arr1[-1]

missing_element(my_list1, my_list2)
print(missing_element(my_list1, my_list2))
