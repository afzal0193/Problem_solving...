v =int(input())
for i in range(v):
    x, y, a = list(map(int, input().split()))
    a = a - y
    a = a // x
    value = a * x
    print(value + y)
