capacity = []
N =int(input())
passenger = 0
for _ in range(N):
    a,b =map(int,input().split())
    passenger = passenger + (b-a)
    capacity.append(passenger)
print(max(capacity))
