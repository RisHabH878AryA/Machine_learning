# Square all numbers in a list without a loop (use comprehension).
arr = [1,2,3,4,5]
arr = [x*x for x in arr]
print(arr)

# using map and lambda
numbers = [x for x in range(1,6)]
result = list(map(lambda x: x*x, numbers))
print(result)   