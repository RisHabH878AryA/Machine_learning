# Count occurrences of each word in a sentence (dict comprehension).
sentence = input("Enter a sentence..")

word_counts = {word: sentence.split().count(word) for word in sentence.split()}
print(word_counts)