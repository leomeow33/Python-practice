n = int(input())
j = 0
ans = []
for i in range(n):
    s = input()
    string = []
    for i in s:
        if len(string)>= 2 and i ==string[-1] ==string[-2]:
            continue
        elif len(string)>=3 and i ==string[-1] and string[-2] == string[-3]:
            continue
        else:
            string.append(i)
    ans.append(''.join(string))
for i in ans:
    print(i)