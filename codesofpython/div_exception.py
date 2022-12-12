a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

try:
    print(f" The answer is {a/b}")

except(ZeroDivisionError):
    print("Infinite")


