a =int(input())
for _ in range(a):
    n =int(input())
    li =list(map(int,input().split()))
    if n <3:
        for i in li:
            print(i,end=" ")
        print()
    else:
        i = 0
        j = len(li)-1
        arr = []
        while i<j:
            arr.append(li[i])
            arr.append(li[j])
            i = i + 1
            j = j - 1
        if n%2 !=0:
            value = li[((i+j)//2)]
            arr.append(value)
        for i in arr:
            print(i,end=" ")
        print()