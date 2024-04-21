# loop

lst = [1, 2, 3, 4]

print(*lst)

for i in lst:
    print(i)

for i in range(len(lst)):
    print(i, lst[i])