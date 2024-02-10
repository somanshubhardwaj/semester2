string=input("Enter a string:")
print("The string is:",string)
if string.isalnum():
    print("The string is alphanumeric.")
elif string.isalpha():
    print("The string is alphabetic.")
elif string.isdigit():
    print("The string is numeric.")
else:
    print("The string is non-alphanumeric.")
