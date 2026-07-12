n=int(input())
for i in range(n):
    n,k=map(int,input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    a=a[:-1]
    s=0
    for j in a:
        s+=j-1
    print(s+sum(a))
