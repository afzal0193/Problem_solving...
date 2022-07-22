def solve(li):
    n =len(li)
    i = 0
    while i< n-1:
        if ((li[i+1] -li[i]))<=1:
            i = i + 1
        else:
            break
    if i ==(n-1):
        return True
    else:
        return False
if __name__ =="__main__":
    n =int(input())
    for i in range(n):
        a =int(input())
        li =list(map(int,input().split()))
        li.sort()
        if solve(li):
            print("YES")
        else:
            print("NO")

