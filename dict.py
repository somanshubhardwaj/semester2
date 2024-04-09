# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print("Updated Dictionary:", my_dict)

# Modifying a value
my_dict['age'] = 35
print("Modified Dictionary:", my_dict)

# Removing a key-value pair
removed_value = my_dict.pop('occupation')
print("Dictionary after removing 'occupation':", my_dict)
print("Removed Value:", removed_value)

# Check if key exists
if 'age' in my_dict:
    print("Age exists in the dictionary")

# Iterating over keys
print("Keys in the dictionary:")
for key in my_dict.keys():
    print(key)

# Iterating over values
print("Values in the dictionary:")
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
print("Key-Value pairs in the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

# Length of dictionary
print("Length of the dictionary:", len(my_dict))

# Clearing the dictionary
my_dict.clear()
print("Cleared Dictionary:", my_dict)
