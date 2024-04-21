input()
lst = list(map(int, input().split()))

for i in range(0, len(lst), 2):
    print(lst[i], end=" ")