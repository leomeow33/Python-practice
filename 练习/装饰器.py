import time
def deco(func):
    def wrapper(a,b):
        start = time.time()
        func(a,b)
        end = time.time()
        res = (end - start)*1000
        print('time is %d ms'%res)
        return func(a,b)
    return wrapper

@deco
def func(a,b):
    time.sleep(a)
    print('slept for %f sec'%a)
    return a

a = 2.66
func(a,5)