a,b =input().split()
a =int(a)
b =int(b)
have_time = 4*60 - b
time = 0
count = 0
for i in range(1,a+1):
    time = time + i*5
    if time<=have_time:
        count = count + 1
print(count)
