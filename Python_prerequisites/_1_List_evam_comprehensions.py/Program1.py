# Filter all even numbers from a list of 1–100.
arr = [i for i in range(0,100) if i%2==0]
print(arr)

# Using lambda and map
numbers = [x for x in range(0,100)]
result = list(map(lambda x: x if x%2==0 else "->" , numbers))
print(result)

# using filter
filter_result = list(filter(lambda x: x%2 ==0, range(1,101)))
print("using filter: ", filter_result)