# Swap keys and values of a dictionary.
diction = {"Hello" : 1, "Mello": 2, "Again": 3}
print(diction)
diction = {values:keys for (keys, values) in zip(diction.keys(), diction.values())}
print(diction)

# Handling duplicates
diction2 = {"Hello" : 1, "Mello": 1, "Again": 3}
result = {}
for k,v in diction2.items():
    result.setdefault(v, []).append(k)
print(result)