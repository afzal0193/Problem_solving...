for i in range(int(input())):
    a,b =input().split()
    a =int(a)
    b =int(b)
    value = abs(a - b)
    div = value // 10
    mod = value % 10
    if mod == 0:
        print(div)
    else:
        print(div + 1)

