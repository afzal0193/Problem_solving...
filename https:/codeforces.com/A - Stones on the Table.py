a =input()
s =input()
n =len(s)
i = 0
count = 0
while i<n-1:
    if s[i] ==s[i+1]:
        count = count + 1
    i = i + 1
print(count)