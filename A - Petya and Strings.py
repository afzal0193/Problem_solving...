a =input().lower()
b =input().lower()
if a.casefold() ==b.casefold():
    print("0")
elif a>b:
    print("1")
else:
    print("-1")
