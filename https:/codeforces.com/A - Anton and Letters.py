a = list(map(str, input().split(",")))
if a[0] == "{}":
    print(0)
else:
    arr = ""
    main_arr = a[1:-1]
    v1 = a[0][-1]
    v2 = a[-1][1]
    for i in main_arr:
        arr = arr + i
    arr = arr + v1
    arr = arr + v2
    val = []
    for i in arr:
        if i.isalpha():
            val.append(i)
    print(len(set(val)))
