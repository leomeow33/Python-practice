n,p = [int(i) for i in input().split()]
l1 = [int(i) for i in input().split()]
res = []
key = 0
for i in range(len(l1)):
    for j in range(i,len(l1)):
        if l1[i] == l1[j] + p or l1[i] == -l1[j] + p:
            if [l1[i],l1[j]] not in res and [l1[j],l1[i]] not in res:
                res.append([l1[i],l1[j]])

print(len(res))



