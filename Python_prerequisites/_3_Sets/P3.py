# Use sets to check if a list has any duplicates efficiently..
l1 = [1,2,3,4,5,5,6,7,7,7]
S1 = set(l1)
if(l1.__len__() == S1.__len__()):
    print("No duplicates")
else:
    print("Has duplicates")