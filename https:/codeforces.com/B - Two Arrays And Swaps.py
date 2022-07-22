a =int(input())
for _ in range(a):
    n,k =list(map(int,input().split()))
    li1 =list(map(int,input().split()))
    li2 =list(map(int,input().split()))
    li1.sort()
    li2.sort()
    li2 = li2[::-1]
    for i in range(k):
        if li1[i]<li2[i]:
            li1[i] = li2[i]
    print(sum(li1))




