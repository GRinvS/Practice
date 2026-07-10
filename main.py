def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z
 
def find_period(s):
    n = len(s)
    z = z_function(s)
    for p in range(1, n):
        if n % p == 0 and z[p] == n - p:
            return p
    return n

print(find_period(input()))