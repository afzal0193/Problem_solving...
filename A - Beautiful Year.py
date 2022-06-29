v =input()
a =int(v)
while True:
    a = a+1
    arr = []
    for i in str(a):
        vl = str(a).count(i)
        if vl ==1:
            arr.append(0)
        else:
            arr.append(vl)
    if not any(arr):
        break
print(a)
