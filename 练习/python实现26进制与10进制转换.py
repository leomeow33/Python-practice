def toTen(s):
    sum = 0
    for i in range(1,len(s)+1):
        sum += (ord(s[-i]) - 97) * (26**(i-1))
    return sum
s1 = list(input())
s2 = list(input())
ans = []
print('s1的十进制表示为：%d,s2的十进制表示为：%d'%(toTen(s1),toTen(s2)))
tmp = toTen(s1) + toTen(s2)
i = 0
while True:
    ans.append(chr(tmp%26 + 97))
    tmp = tmp // 26
    if tmp == 0:
        break
print(''.join(ans)[::-1])  #append导致在列表中高位在最后，低位在最前，所以反序输出即可输出正确序列
