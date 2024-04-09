# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing
print("Sliced list:", my_list[1:4])

# Appending
my_list.append(6)
print("Appended list:", my_list)

# Extending
my_list.extend([7, 8, 9])
print("Extended list:", my_list)

# Inserting
my_list.insert(2, 10)
print("List after insertion:", my_list)

# Removing
my_list.remove(3)
print("List after removal of element 3:", my_list)

# Popping
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Index
index = my_list.index(4)
print("Index of element 4:", index)

# Count
count = my_list.count(2)
print("Count of element 2:", count)

# Sorting
my_list.sort()
print("Sorted list:", my_list)

# Reversing
my_list.reverse()
print("Reversed list:", my_list)

# Copying
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Clearing
my_list.clear()
print("Cleared list:", my_list)
