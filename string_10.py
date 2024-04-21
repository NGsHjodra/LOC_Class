# loops

s = "string"

for i in s:
    print(i)

print()

for i in range(len(s)):
    print(i, s[i])

print()

for i, v in enumerate(s):
    print(i, v)