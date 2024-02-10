string=input("Enter a stringm:")
print("The string is:",string)
if string.upper():
    print("The string in uppercase is:",string.upper())
elif string.lower():
    print("The string in lowercase is:",string.lower())
elif string.title():
    print("The string in titlecase is:",string.title())
else:
    print("The string is non-alphanumeric.")
