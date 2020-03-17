n = int(input())
num = [int(i) for i in input().split()]
energy = 1
tmpenergy = 1
dif = 0
for energy in range(1,9999999):
    tmpenergy = energy
    for i in range(n):
        dif = num[i] - tmpenergy
        tmpenergy -= dif
        if tmpenergy < 0 :
            break
        if i == n-1:
            print(energy)
            break
    if i ==n-1 and tmpenergy >0:
        break