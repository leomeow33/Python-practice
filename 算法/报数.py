c = [i for i in range(1,101)]  #c0=1 c1=2 c2=3 c3=4   m=3时，  c2退出。 c3变成c0  c0 c1续到最后   c3: 1
m = int(input())
if m <=1 or m >= 100:
    print('ERROR!')
else:
    while len(c) >= m:
        c.pop(m-1)
        c = c + c[:m-1]
        c = c[m-1:]
c.sort()
c = [str(i) for i in c]
print(','.join(c))