evenodd = lambda x: "Even" if x % 2 == 0 else "odd"
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennum = list(filter(lambda x: x % 2 == 0, num))
print("Even number:", evennum)
sqnum = list(map(lambda x: x ** 2, num))
print("SQUAREnum:", sqnum)