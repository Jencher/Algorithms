my_list1 = [1, 6, 10, 7, 2, 11]
my_list2 = [975, 25]

# to summ up two lists
print(my_list1 + my_list2)

# to print an element by its index [0]
print(my_list1[0])

# to add an element to the end of list
my_list1.append(77)
print(my_list1)

# to clear list
# my_list1.clear()


print(my_list1.count(10))

# to print the index of number 10   #2
print(my_list1.index(10))

# to add an element in a certain place (after 1 we want to add 77)
my_list1.insert(1, 77)
print(my_list1)

# to remove an element with index [0]  #1
my_list1.pop(0)
print(my_list1)

#  to remove an element by its value (7)  # 77. 6, 10, 2, 11, 77
my_list1.remove(7)
print(my_list1)

# to reverse list
my_list1.reverse()
print(my_list1)

# to sort list  (to organize from smallest to biggest)
my_list1.sort()
print(my_list1)

# to count the length
print(len(my_list1))
