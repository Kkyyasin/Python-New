print(range(1, 15))
print(*range(1, 15))
print(range(10))
print(*range(1, 5, 2), sep="\n-\n")
for i in range(1, 15):
    print(i, end="-")
for i in range(15):
    print(i*"*")
