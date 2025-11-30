print("Hello i can work like that too ")
# Find common elements between two lists.

l1 = [2,1,3,4,5]
l2 = [2,1,6,7,8]
S1 = set(l1)
S2 = set(l2)
print(S1, S2)
S3 = S1.intersection(S2)
print(list(S3))