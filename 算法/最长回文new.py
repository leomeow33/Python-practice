#返回字符串中的最长回文
#思路是两个游标，对每个s从左侧开始检测是否是最长回文
#然后通过s = s[:len(s)-1:]切割s的最右侧一个字符
s = input()
strtmp = ''
maxlen = 0
res = -1
l = len(s)
while len(s) > 2:
    for i in range(len(s)-1):
        if s[i::] == s[:-len(s)-1+i:-1]:
            if len(s[i::]) > maxlen:
                maxlen = len(s[i::])
                res = i         #记录下此刻的下标
                strtmp = s     #记录下此刻的字符串
    s = s[:len(s)-1:]
if res != -1:
    print(strtmp[res::])
else:
    print('not found')
