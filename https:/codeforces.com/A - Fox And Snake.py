a,b =map(int,input().split())
j = 0
for i in range(a):
    if i %2==0:
        print("#"*b)
    else:
        if j%2==0:
            print("."*(b-1)+"#")
        else:
            print("#"+(b-1)*".")
        j = j + 1


