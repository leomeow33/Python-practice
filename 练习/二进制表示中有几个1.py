def countBits(n) :
    count = 0
    while n != 0 :
        n = n & (n-1)
        count += 1
    return count

num = int(input())
ans = countBits(num)
print(str(num) + '的二进制表示中有' + str(ans) + '个1')