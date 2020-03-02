def reverse_str(str):
    list = str.split()
    for i in range(len(list)):   #for i in range(len(x))是遍历的最常用方法，会遍历到0,1,2...len(x)-1，遍历次数还是len(x)
        list[i] = list[i][::-1]
    str = ' '.join(list)
    return str

str = input('输入欲内部翻转的字符串:')
print('翻转前的字符串:',str)
str = reverse_str(str)
print('翻转后的字符串:',str)

#python 函数的参数传递：
#不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
#比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
#若一定要用函数处理字符串，建议使用return str的方式来保证字符串被成功处理,若默认返回none则会处理失败，因为字符串类型不可变。