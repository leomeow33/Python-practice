n = int(input())
d = {}
ans = 0
for i in range(n):
    m = int(input())
    for j in range(m):
        l = [int(i) for i in input().split()]
        tmp = {}
        for k in range(l[0]):
            index = l[2*k+1]*1000000000 + l[2*k+2]
            if index in d:
                tmp[index] = d[index] + 1
                ans = max(tmp[index],ans)
            else:
                tmp[index] = 1
            d = tmp
print(ans)