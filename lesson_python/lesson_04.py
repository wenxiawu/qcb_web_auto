'''
for循环：遍历 数据对象里的所有元素： str,list,tuple,dict
for  变量名  in  数据对象:
    子代码（循环体）
循环多少次由什么决定的？---元素个数
中断： break(跳出整个循环)   continue(结束本次循环)

range()  ----内置函数：生成一个整数序列；1,2,3,4,5,6
跟 for 循环一起使用：
    start-开始  ====默认值为0
    stop-结束  ====取头不取尾
    step-步长
'''
count = 0
list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝','十又','bingo','陌上寸草','大丑']
for name in list1:
    if name=="荷花鱼":
        # break    #跳出整个循环
        continue   #结束本次循环
    print(name)
    print("*" * 20)
    count += 1
print(count)
print(len(list1))

for i in range(0,6,2):
    print(i)

'''
函数：将一段代码封装成函数，方便调用。  =======提高代码的复用率，提高执行的效率
语法：
def 函数名():
    子代码(函数体)  -----  实现的功能
注意：函数只定义了 ，没有调用的话不会执行；
如何调用函数？ -------写函数名，直接进行调用

函数里不固定的数据 -- 定义成函数的参数----括号里
1)形参 -- 函数定义的时候  定义的
2)实参 -- 调用函数传入参数

参数定义的类型：
1)必备参数：定义了就必须要传入的参数---不传会报错
2)默认参数（缺省参数）：可以定义的时候赋值一个默认值 
    -- 调用的时候可以不传入;
    -- 可以传，会替换默认值
    注意：默认参数必须在必备参数后面！！！
3)不定长参数 --- 接收不确定数量、个数的参数 
    *args：可以选择不传，也可以选择传入(1个、多个) == 元组接收---传参方式：位置传参
    注意：等前面的必备参数和默认参数都接收完了，剩下的参数都给不定长参数接收
    **kwargs：字典接收，传参的方式----关键字传参
    
传参的方式类型:
1)位置传参：按照位置参数传入
2)关键字传参：指定参数名来进行传参，不关心顺序 ----可靠
3)混合传参：注意关键字传参必须跟在位置传参后面
'''
def good_job(salary,bonus,subsidy=500,*args,**kwargs):     #定义 ---- 函数名  ===函数的参数--形参(变量替代)
    sum1 = salary + bonus + subsidy     # sum1 实现功能
    print("salary的值:{}".format(salary))
    print("bonus的值:{}".format(bonus))
    print("subsidy的值:{}".format(subsidy))
    print("args的值:{}".format(args))
    print("kwargs的值:{}".format(kwargs))
    for i in args:
        sum1 += i
    for j in kwargs:
        # sum1 += kwargs.get(j)  #通过key  --- 取到value
        sum1 += kwargs[j]
    print("这个工作的工资总和是{}".format(sum1))
# good_job(salary=8000, bonus=2000, subsidy=800, aa=50, bb=100, cc=200, dd=300) #用函数名进行函数的调用 -- 函数才会被执行  ---实参
good_job(8000,2000,800,100,200,300,a=50,bb=100,cc=200,dd=300)

'''
有进有出： 进---参数，出---返回值
返回值：函数可以给到外面的人用的数据 ---- 调用函数的时候  可以获取到这个返回值  -----return
1)定义
2)调用-- 变量接收返回值
3)如果没有返回值 --- None，可以有return  ；可以有多个---元组保存
4)注意：返回值卸载函数的最后 --- 标志着函数的结束
'''
def good_job(salary,bonus,subsidy=500,*args,**kwargs):     #定义 ---- 函数名  ===函数的参数--形参(变量替代)
    sum1 = salary + bonus + subsidy     # sum1 实现功能
    for i in args:
        sum1 += i
    for j in kwargs:
        sum1 += kwargs[j]
    return sum1,salary  # 定义了一个返回值 ===两个返回值，用逗号隔开

result = good_job(8000,2000,800)
print(result)

'''
内置函数：
print()
input()
type()
instance()
len()
replace,count,find,index,append,insert,pop,remove,update  ----数据类型的内置方法
str(),float(),int(),list(),tuple(),dict(),bool(),set()
range() ----生成整数序列
'''

'''
作业：
1. 把字符串转成列表 - list()
'''
str1 = "hello world"
list1 = []
for i in str1:
    list1.append(i)
print(list1)

'''
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
'''
def add_fun(num):
    sum = 0
    num = int(input("请输入正数："))   #字符串
    for i in range(num):
        sum += i
    print(sum)

'''
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
'''
def function_len(object):
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        leng = len(object)
        if leng >= 5:
            print("True")
        else:
            print("False")
    else:
        print("数据类型不能计算长度！")   #容错性友好
function_len([1,2,3,4,5])

print(5/3)






















