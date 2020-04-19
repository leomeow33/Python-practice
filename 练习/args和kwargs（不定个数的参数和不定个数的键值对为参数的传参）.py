def func1(a,*c):
    print('first',a)
    for i in c:
        print('lalala',i)




def func2(a,**c):
    print('first',a)
    for i,j in c.items():
        print('%s is %s'%(i,j))
    print(c)


func1('miao?',123,345,678,'31235')
func2('miao?',name = 123,age = 555,sex = 'booooy')