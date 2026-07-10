num = int(input())
f = []
for i in range(num):
    a = input()
    b = a.split(" ")
    c=[]
    for j in b:
        c.append(int(j))
    c = sorted(c)
    c.reverse()
    d = c[0]
    for h in range(1,len(c)):
        d -= c[h]
    f.append(d)
for i in range(num):
    print(f[i])
