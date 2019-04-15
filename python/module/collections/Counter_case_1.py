# https://blog.csdn.net/u014755493/article/details/69812244

from collections import Counter


# elements() 按照counter的计数，重复返回元素




c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

 


# most_common(n) 按照counter的计数，按照降序，返回前n项组成的list; n忽略时返回全部
print(Counter('abracadabra').most_common(3))
# [('a', 5), ('r', 2), ('b', 2)]

 



# subtract([iterable-or-mapping]) counter按照相应的元素，计数相减
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
 




# update([iterable-or-mapping]) 不同于字典的update方法，这里更新counter时，相同的key的value值相加而不是覆盖
# 实例化 Counter 时， 实际也是调用这个方法
 
 
# Counter 间的数学集合操作
c = Counter(a=3, b=1, c=5)
d = Counter(a=1, b=2, d=4)

print(c + d)				# counter相加, 相同的key的value相加
# Counter({'c': 5, 'a': 4, 'd': 4, 'b': 3})

print(c - d)                # counter相减, 相同的key的value相减，只保留正值得value
# Counter({'c': 5, 'a': 2})

print(c & d)				# 交集:  取两者都有的key,value取小的那一个
# Counter({'a': 1, 'b': 1})

print(c | d)				# 并集:  汇聚所有的key, key相同的情况下，取大的value
# Counter({'c': 5, 'd': 4, 'a': 3, 'b': 2})





# 常见做法:
print(c.values())
print(sum(c.values()))			# 继承自字典的.values()方法返回values的列表，再求和


print(list(c))					# 返回key组成的list


print(set(c))					# 返回key组成的set


print(dict(c))					# 转化成字典


print(c.items())				# 转化成(元素，计数值)组成的列表


# Counter(dict(list_of_pairs))    # 从(元素，计数值)组成的列表转化成Counter


print(c.most_common(2))       	# 最大n(2)个计数的(元素，计数值)组成的列表
# [('c', 5), ('a', 3)]

c += Counter()                  # 利用counter的相加来去除负值和0的值

c.clear()                       # 继承自字典的.clear()方法，清空counter