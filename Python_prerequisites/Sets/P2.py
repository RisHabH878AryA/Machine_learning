# Remove duplicates from a list while preserving order (slightly tricky!).
l1 = [3,5,3,3,5,4]

S1 = list(set(l1))

result = []

for y in range(l1.__len__()):
    for x in range(S1.__len__()):
        if S1[x] == l1[y] and S1[x] not in result:
            result.append(S1[x])
            
print(result)