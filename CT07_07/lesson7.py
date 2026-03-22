# Task 1

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]
# list3 = list1 + list2
# print(list3)

# Task 2

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]
# list3 = list1 + list2
# print(list3) = sorted(list3)
# print(list3)

# Task 3

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3
# sliced = fruits[3:6]
# print(sliced)

# Task 4

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# length = len(fruits)
# midpoint = length // 2
# split1 = fruits[:midpoint]
# split2 = fruits[midpoint:]
# print(split1)
# print(split2)

# Task 5

# common = []

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# for item in list1:
#     if item in list2:
#         common.append(item)
# print(common)

# Task 6

# unique = []

# list1 = ["Apple", "Banana", "Cherry", "Cherry"]
# list2 = ["Cherry", "Durian", "Durian", "Figs"]

# for i in list1:
#     if i not in unique:
#         unique.append(i)

# for i in list2:
#     if i not in unique:
#         unique .append(i)

# print(unique)

## Task 7: Merging Lists with Conditions
# You have been given the index number of 2 groups of students.
# However, only students with even index number is allowed
# to come into the room. Create a Python script that will
# merge the 2 lists, including only the elements that are
# even from both.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# 1. Merge the lists using a list comprehension with a
#    condition.
# 2. Print the new list.

# even = []
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# merge = list1 + list2

# for i in merge:
#     if i % 2 == 0:
#         even.append(i)

# print(even)

## Task 8: Nested List Splitting
# You are given a nested list of 3 groups of students that
# are each seated in a pair. However, you want to unpack
# the nested lists in order to have a list of all students.

# nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. Use a loop or list comprehension to flatten the list.
# 2. Print the flattened list.

# nested_list = [[1, 2], [3, 4], [5, 6]]

# for list in nested_list:
#     for number in list:
#         print(number)

## Task 9: Partitioning a List into Smaller Lists
# You have been tasked to divide a class of 9 students
# into groups of 3.

# Given a list and a size, split the list into multiple
# sub-lists where each sub-list is of the given size.

# students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# size = 3

# 1. Use a loop to create sub-lists of the specified size.
# 2. Print the sub-lists.

students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3