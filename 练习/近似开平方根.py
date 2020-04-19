a = float(input())  #欲开的平方根
num = float(input())  #精度

def sqrt(a):
    start = 0
    res= a/2
    end = a
    while abs(res**2 - a) >num:

        if res**2 > a:
            end = res
            res = (start+res)/2
        if res**2 < a:
            start = res
            res = (end + res)/2

    return res
asqrt = sqrt(a)
print(asqrt,end = '')
print('为a的平方根')