arr = []
for _ in range(5):
    li =list(map(int,input().split()))
    arr.append(li)
a = 0
ar1 = 0
for i in arr:
    if 1 in i:
        a = i.index(1) + 1
        ar1 = arr.index(i) + 1
v = abs(3 - ar1)
v2 = abs(3 - a)
print(v+v2)
