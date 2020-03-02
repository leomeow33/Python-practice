def maopao_sort(list):
    b = len(list)
    for i in range(b):
        for j in range(b - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('原列表为:',list)
maopao_sort(list)
print('新列表为:',list)


