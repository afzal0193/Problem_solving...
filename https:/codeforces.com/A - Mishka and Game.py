n =int(input())
micka = []
charis = []
for _ in range(n):
    m,c =list(map(int,input().split()))
    if m>c:
        micka.append(1)
    elif c>m:
        charis.append(1)
if len(micka)>len(charis):
    print("Mishka")
elif len(micka)<len(charis):
    print("Chris")
else:
    print("Friendship is magic!^^")