n = int(input())  #几个字符串
long = int(input()) #第几长
thelen = 0 #所求字符串的长度
s = []
sl = [0]*n

for i in range(n):
    s.append(input())
for i in range(len(s)):
    sl[i] = len(s[i])
sl = list(set(sl)) #去重
sl.sort(reverse = True)
if (long - 1) in range(len(sl)):
    thelen = sl[long - 1]
    print(thelen)
else:
    print(max(sl))
