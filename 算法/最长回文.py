'''链接：https://www.nowcoder.com/questionTerminal/b2a424607bd14f26ab0e22ba84cd44b9
来源：牛客网

对称子字符串的最大长度

题目：输入一个字符串，输出该字符串中对称的子字符串的最大长度。
比如输入字符串“google”，由于该字符串里最长的对称子字符串是“goog”，因此输出4。

分析：可能很多人都写过判断一个字符串是不是对称的函数，这个题目可以看成是该函数的加强版。'''
def s(x):
    for i in range(int(len(x)/2)):
        if x[i] != x[len(x)-1-i]:
            return False
    return True
a, m = input(), 1
for l in range(2, len(a)+1):
    for t in range(len(a)+1-l):
        if(s(a[t:t+l])):
            m = l
print(m)