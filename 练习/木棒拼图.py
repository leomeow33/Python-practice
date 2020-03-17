n = int(input())
ans = []
for i in range(n):
    op,l = [int(ele) for ele in input().split()]
    if op == 1:
        ans.append(l)
    elif op == 2:
        ans.remove(l)
    if sum(ans) <= 2*max(ans):
        print('No')
    else :
        print('Yes')
