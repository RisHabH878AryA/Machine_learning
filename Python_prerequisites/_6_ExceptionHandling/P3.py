# Try converting string to numbers , catch 'ValueError' if conversion fails.

str1 = input("Enter a number")

try:
    num = int(str1)
    print(f"num = {num}")
except ValueError as e:
    print(e)