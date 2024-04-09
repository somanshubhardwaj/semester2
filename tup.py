# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced tuple:", my_tuple[1:4])

# Concatenation
concatenated_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", concatenated_tuple)

# Repetition
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Length
length = len(my_tuple)
print("Length of tuple:", length)

# Membership test
is_present = 3 in my_tuple
print("Is 3 present in the tuple?", is_present)

# Index
index = my_tuple.index(4)
print("Index of element 4:", index)

# Count
count = my_tuple.count(2)
print("Count of element 2:", count)
