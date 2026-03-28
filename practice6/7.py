from functools import reduce

res = reduce(lambda a, b: a + b, [1, 2, 3])
print(res)

items = ["a", "b", "c"]

for i, val in enumerate(items):
    print(i, val)

a = [1, 2]
b = ["x", "y"]

print(list(zip(a, b)))