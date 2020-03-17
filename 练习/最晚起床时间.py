def timetomin(l):
    return(l[0]*60 + l[1])
def mintotime(min):
    tmp = [0]*2
    tmp[0] = min//60
    tmp[1] = min%60
    return tmp
def bsearch(list,num):
    min = 0
    max = len(list) - 1
    i = 0
    while True:
        i += 1
        mid = (min+max)//2
        if list[mid] < num:
            min = mid + 1
        elif list[mid] == num:
            return num
        elif list[mid] > num:
            max = mid -1
n = int(input())
alarmtmp  = []
alarm = []
ddltmp = []
ddl = 0
for i in range(n):
    alarmtmp.append([int(i) for i in input().split()])
for i in alarmtmp:
    alarm.append(timetomin(i))
m = int(input())
ddltmp = [int(i) for i in input().split()]
# 7:30 ala  50min   8:10
ddl = timetomin(ddltmp)
ddl -= m
for i in range(1,len(alarm)):
    if alarm[i] > ddl and alarm[i-1]<= ddl:
        print(' '.join(str(i) for i in mintotime(alarm[i-1])))
        break