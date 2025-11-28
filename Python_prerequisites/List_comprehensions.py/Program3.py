# Flatten a list of lists in one line.
arr = [[1,3,5,7,9], [0,2,4,6,8]]
arr2 = []
for x in arr:
    for y in x:
        arr2.append(y)
print(arr2)