def maopao_sort(list):
    b = len(list) - 1               #大循环进行i-1次，即可把i-1个数从右往左从大到小放好，这样最左边就是最小的数，故b = len(list) - 1
    for i in range(b):
        for j in range(b - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('原列表为:',list)
maopao_sort(list)
print('新列表为:',list)


