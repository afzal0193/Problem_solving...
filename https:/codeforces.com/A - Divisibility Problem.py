a = int(input())
for i in range(a):
    a, b = map(int, input().split())
    if int(a) % int(b) == 0:
        print(0)
    else:
        v = a // b
        main_value = b * (v + 1)
        ans = main_value - a
        print(ans)
