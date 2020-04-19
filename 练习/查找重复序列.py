n = int(input())
seq = []
dic = {}
res = [[] for i in range(n)]
t = 0
for i in range(n):
    l = int(input())
    seq.append(input())
for i in range(len(seq)):
    if seq[i] not in dic:
        dic[seq[i]] = i
    else:
        if dic[seq[i]] not in res[dic[seq[i]]]:
             res[dic[seq[i]]].append(dic[seq[i]])  #加第一个重复序列的坐标
        res[dic[seq[i]]].append(i)   #加第二个重复序列的坐标
for i in res:
    if i != []:
        print(' '.join(str(j) for j in i))
if res == [[] for i in range(n)]:
    print('no')


