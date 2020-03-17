import collections
n = int(input())
a = list(map(int, input().split()))
d = collections.defaultdict(set)
inex = 1
# 把相同兴趣度的用户存在字典中
for i in a:
    d[i].add(inex)
    inex += 1
m = int(input())
for i in range(m):
    b = list(map(int, input().split()))
    count = 0
    # 判断字典中是否存在喜好值为k的键名
    if d[b[2]]:
        # 遍历对应键名下的键值，当键值在给定的范围中，则+1
        for j in d[b[2]]:
            if b[0] <= j <= b[1]:
                count += 1
    print(count)