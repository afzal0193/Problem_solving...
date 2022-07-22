for _ in range(int(input())):
  n=int(input())
  if n%4==0:
    print("YES")
    for i in range(1,n//2+1):
      print(2*i, end=' ')
    for i in range(1,n//2):
      print(2*i-1, end=' ')
    print(n//2+(n)-1)
  else:
    print("NO")
