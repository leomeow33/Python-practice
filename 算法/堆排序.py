#python实现堆排序
def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[largest]<arr[left]:
        largest=left
    if right<n and arr[largest]<arr[right]:
        largest=right
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]  #python是地址引用，交换
        heapify(arr,n,largest) #下沉式调整

def heapsort(arr):
    n=len(arr)
    # 将序列构造成大根堆
    for i in range(n-1,-1,-1):
        heapify(arr,n,i)

    #把最大值交换到最后位置，再重新调整为堆，升序排列
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[3,4,1,99,6,0,23,43,36,88,8,8,99999999]
heapsort(arr)
for i in range(len(arr)):
    print(arr[i])
