from functools import reduce

words = ["hello ", "world ", "python ", "programming"]
conc_string = reduce(lambda x, y: x + y, words)
print(conc_string)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x + y, num)
print("sum of element", sum)
