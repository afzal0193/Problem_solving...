for i in range(int(input())):
    a = int(input())
    mod1 = a % 1000
    val1 = a - mod1
    mod2 = mod1 % 100
    val2 = mod1 - mod2
    mod3 = mod2 % 10
    val3 = mod2 - mod3
    arr = []
    if val2 is not 0:
        arr.append(str(val2))
    if val3 is not 0:
        arr.append(str(val3))
    if mod3 is not 0:
        arr.append(str(mod3))
    if val1 is not 0:
        arr.append(str(val1))
    print(len(arr))
    print(" ".join(arr))
