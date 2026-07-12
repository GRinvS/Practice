t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    left = 0
    right = n - 1
    sunk = 0
    while left <= right and k > 0:
        if left == right:
            if k >= a[left]:
                sunk += 1
            break
        min_hp = min(a[left], a[right])
        if k >= min_hp * 2:
            a[left] -= min_hp
            a[right] -= min_hp
            k -= min_hp * 2
            if a[left] == 0:
                sunk += 1
                left += 1
            if a[right] == 0:
                sunk += 1
                right -= 1
        else:
            if k % 2 == 1:
                if a[left] <= (k + 1) // 2:
                    sunk += 1
                break
            else:
                if a[left] <= k // 2:
                    sunk += 1
                if a[right] <= k // 2:
                    sunk += 1
                break
    print(sunk)
