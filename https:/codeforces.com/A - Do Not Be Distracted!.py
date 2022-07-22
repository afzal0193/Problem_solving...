def solve(n,data):
    stack =["0"]
    for i in data:
        if stack[-1] !=i and i in stack:
            return False
        stack.append(i)
    return  True
if __name__ =="__main__":
    for i in range(int(input())):
        n =int(input())
        data =input()
        if solve(n,data):
            print("YES")
        else:
            print("NO")