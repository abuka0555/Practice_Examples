with open("test.txt", "w") as f:
    f.write("Hello\n")

with open("test.txt", "a") as f:
    f.write("World\n")


with open("test.txt", "r") as f:
    print(f.read())