# Read a text file, count frequency of each word.

with open("Book.txt", "w") as f:
    f.write("where have come and and and and and where shall we end if dreams can't come true, then why not pretend?")
    
with open("Book.txt", "r") as f:
    read_str = f.read()
    
print(read_str, type(read_str))
read_str = read_str.strip().split(" ")
print(read_str, type(read_str))

word_freq = {}
# print(word_freq["Name"] + 1)

for word in read_str:
    if word in word_freq.keys():
        count = word_freq[word] + 1
    else:
        count = 1
    word_freq[word] = count
    
print(word_freq)