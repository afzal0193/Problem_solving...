a =int(input())
for i in range(1,a+1):
    n =input()
    if n =="word":
        print("word")
    elif len(n)<=10:
        print(n)
    else:
        l = len(n) - 2
        print("%s%i%s" % (n[0], l, n[-1]))