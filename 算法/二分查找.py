def binarysearch(list,num):
   min = 0 #最小的下标
   max = len(list)-1 #最大的下标
   i = 0
   while True:
      i+=1
      mid=(min+max)//2
      if num < list[mid]:
         max = mid - 1   #中间的已经猜过，故-1
      if num == list[mid]:
         print('找到数据，其为%d，查找%d次'%(num,i))
         break
      if num > list[mid]:
         min = mid + 1  #中间的已经猜过，故+1

list = [i for i in range(0,1001)]
num = 499
binarysearch(list,num)

