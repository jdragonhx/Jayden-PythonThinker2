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

common = []

list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

for item in list1:
    if item in list2:
        common.append(item)
print(common)
