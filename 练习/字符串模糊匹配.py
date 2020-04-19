import re
s = input()
str = input()
str = str.replace('?', '\w{1,3}?')
p = re.compile('^' + str)
res = re.findall(p, s)
if res:
    l = len(res[0])
    for i in res:
        if len(i) < l:
            l = len(i)
    print(l)
else:
    print('-1')

