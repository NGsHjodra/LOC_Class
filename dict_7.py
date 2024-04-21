"""
a 70
b 30
c 40
d 50
"""

d = {}
for _ in range(4):
    key, value = input().split()
    d.update({key:int(value)})

print(d)
print(d.get("a"))