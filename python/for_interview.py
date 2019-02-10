
''' 
__Author__:沂水寒城 
功能：一些面试习题的练习和测试
''' 
 
import random
from functools import reduce
from operator import mul
 
 
def extendList(val, list=[]):
    '''
    实际发生的事情是，新的默认列表仅仅只在函数被定义时创建一次。随后当 extendList 没有被指定的列
    表参数调用的时候，其使用的是同一个列表。这就是为什么当函数被定义的时候，表达式是用默认参数被计算，而
    不是它被调用的时候,list1 和 list3 是操作的相同的列表。而list2是操作的它创建的独立的列表（通过传递它自
    己的空列表作为list参数的值）
    '''
    list.append(val)
    return list
 
 
def squ(x):
    return x*x
 
 
#最Pythonic的代码
def some_test():
    '''
    '''
    num_list = [-2,-1,0,1,2,3,4,5]
    
    #交换首尾两个数字
    num_list[0],    num_list[len(num_list)-1]   =   num_list[len(num_list)-1],  num_list[0]

    #列表推导式,求列表中每个数的平方，这里也可以使用lambda函数来做
    new_list = [one*one for one in num_list]
    
    #new_list2=map(lambda x: x*x, [y for y in range(10)] )
    #print [lambda x:x+1 for x in num_list]
    print('所有元素的平方为：', list(map(lambda x: x*x, num_list)))
    print('所有元素的平方为：', list(map(squ, num_list)))
    print('所有元素的绝对值为：', list(map(lambda x: abs(x), num_list)))
    print('所有为负数的元素为：', list(filter(lambda x: x < 0, num_list)))
    print('所有元素的和为：', reduce(lambda x,y: x+y, num_list))
 
 
def print_mutiple():
    '''
    打印乘法表
    '''
    for i in range(1,10):
        one_line = ''
        for j in range(1,i+1):
            one_line += '{0}*{1}={2}'.format(j,i,i*j)+' '
        print(one_line+'\n')
 
 
def create_dict():
    '''
    创建字典,除了列举出来的还可以直接赋值创建、通过关键字dict和关键字参数创建等
    '''
    id_list = ['20123456', '20124567', '20127890']
    name_list = ['Mike', 'Jack', 'Tom']
    test_tuple = [('20123456', 'Mike'), ('20124567', 'Jack'), ('20127890', 'Tom')]
    one_dict = dict(zip(id_list, name_list))
    
    print('zip方法创建的字典为：', one_dict)
    print('fromkeys方法创建的字典为:', dict.fromkeys(id_list))
    print('二元组列表创建的字典为：', dict(test_tuple))
    print('迭代器方式输出字典中的内容:')
    
    for i in one_dict.iteritems(): #迭代对象每次只能取出一个使用for循环遍历输出，数据量大的时候速度更快
        print(i)
    
    print('----------------------------------------------------------------------------')
    
    for j in one_dict.items():  #迭代器，一次性取出字典中所有内容
        print(j)
 
 
def tuple2_list(one_tuple):
    '''
    元祖转化为列表
    '''
    return [i if not isinstance(i, tuple) else tuple2_list(i) for i in one_tuple]
 
 
def list_test():
    '''
    一些简单的列表操作：求和，最值、乘积、索引元素对输出、字符串化输出
    '''
    num_list = [-3,4,3,2,8] 
    num_list2 = [4,5,6,7,8,9]
    one_tuple = ('A','B','C','D','E')  
    total = sum(num_list)  #列表求和
    max_value = max(num_list) #列表求最大值
    min_value = min(num_list) #列表求最小值l
    multiple = reduce(mul, num_list, 1) #默认值传1以防空列表报错
    
    print('最大值为：', max_value)
    print('最小值为：', min_value)
    print('总和为：', total)
    print('乘积为：', multiple)
    print('输出列表中元素下标和元素值为：')
    
    for index, ele in enumerate(num_list):
        print('下标{0}处的元素为：{1}'.format(index, ele))
    
    print('将列表中元素拼接输出：', ''.join([str(x) for x in num_list]))
    print('列表转化为元组形式为：', tuple(num_list))
    print('元祖转化为列表形式为：', tuple2_list(one_tuple))
    print('num_list和num_list2的交集为：', [one for one in num_list if one in num_list2])
    print('num_list和num_list2的差集为：', [one for one in num_list if one not in num_list2])
    print('num_list和num_list2的并集为：', num_list+num_list2)
 
 
def simple_num():
    '''
    简单的赋值
    '''
    one = 9
    two = 90 if one > 10 else 19
    print('two is:', two)
 
 
def random_test():
    '''
    简单常用的random模块函数使用
    '''
    num_list = [3,5,6,9,0,1,2,7,18,21,34,67,91]
    print('输出一个指定范围1--1000的随机整数：', random.randint(1,1000))
    print('输出一个随机的浮点数0-1之间: ', random.random())
    print('输出一个指定上下界的随机的浮点数为：', random.uniform(12,20))
    print('输出num_list中一个随机数: ', random.choice(num_list))
    print('输出对num_list列表随机采样n位的结果为：', random.sample(num_list, 5))
    random.shuffle(num_list)
    print('输出打乱顺序后的列表为：', num_list)
 
 
def str_test():
    '''
    关于字符串的一些简单方法使用
    '''
    one_str = 'abdefEFdf12895sdsAd '
    one_str = one_str.strip()
    
    print('转化为大写：', one_str.upper())
    print('转化为小写：', one_str.lower())
    
    print('检查字符串是否由字母字符组成:', one_str.isalnum())
    print('检查字符串是否由字母字符组成:', one_str.isalpha())
    print('检查字符串是否由数字字符组成:', one_str.isdigit())
    
    print('替换字符a:', one_str.replace('a', 'Z'))
    print('分割字符串：', one_str.split('E'))
 
 
def set_test():
    '''
    set的一些简单使用方法举例
    '''
    one_str = 'abgkGJdir234jd'
    two_str = 'djkg89034jmhjG'
    one_set = set(one_str)
    two_set = set(two_str)
    
    print('one_str转化为集合为：', one_set)
    print('two_str转化为集合为：', two_set)
    
    #单纯在，交、并、差的运算上以及去重的操作上set的确是由于list的操作的
    print('one_set和two_set交集为：', one_set & two_set)
    print('one_set和two_set并集为：', one_set | two_set)
    print('one_set和two_set差集为：', one_set - two_set)
    print('one_set和two_set对称差集为：', one_set ^ two_set)
 
 
if __name__ == '__main__':
    #extendList测试
    list1 = extendList(10)
    list2 = extendList(123,[])
    list3 = extendList('a')
    
    print("list1 = %s" % list1)
    print("list2 = %s" % list2)
    print("list3 = %s" % list3)
 
    #some_test测试
    some_test()
 
    #打印乘法表
    print_mutiple()
 
    #创建字典测试
    create_dict()
 
    #列表的简单测试
    list_test()
 
    #简单的赋值
    simple_num()
 
    #random模块的简单使用
    random_test()
 
    #字符串处理的一些常用方法
    str_test()
