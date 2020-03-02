for num in range(0,50):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print('%d等于%d * %d'%(num,i,j))
            break
    else:
        print(num,'是一个质数')


