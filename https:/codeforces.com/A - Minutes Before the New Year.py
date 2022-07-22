a =int(input())
for i in range(a):
    n,m =list(map(int,input().split()))
    print(1440-((60*n)+m))