with open("file.txt", "w") as f:
    f.write("A\n")

with open("file.txt", "a") as f:
    f.write("B\n")

with open("file.txt") as f:
    print(f.read())