try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Error: Invalid input, please enter a valid number")
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("Division result:", y)
finally:
    print("This block always executes, regardless of whether an exception occurred or not")
