a = int(input())
count = 0
for i in range(a):
    a, b, c = map(int, input().split())
    value = int(a) + int(b) + int(c)
    if value >= 2:
        count = count + 1
print(count)