a =int(input())
li =list(map(int,input().split()))
li2 =list(map(int,input().split()))
value = set(li + li2)
if 0 in value:
    value.remove(0)
last = 0
for i in value:
    last = last + 1
if a ==3 or a ==6:
    print("Oh, my keyboard!")
elif last==a:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")