# Open a file that doesn’t exist and catch the exception gracefully.
try:
    with open("Meow.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    # print("File named : 'Meow.txt' not found!", e)
    print(e)