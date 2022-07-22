n =int(input())
for i in range(n):
    value = int(input())
    if value % 2 == 0:
        print(int(value // 2) - 1)
    else:
        print(int(value / 2))