def is_divisable(a,b): #chack Numbers are divisable or not
    if a%b ==0:
        return True
    return False
arr = []
a =int(input())
for i in range(1,5+1):  #this is main code of problems
    if is_divisable(a,i):
        val = a//i
        arr.append(val)
print(min(arr))
