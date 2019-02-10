def square(x) :            # 计算平方数
	return x ** 2

m1 = map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
print(list(m1))

m2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(list(m2))
 
# 提供了两个列表，对相同位置的列表数据进行相加
m3 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(m3))



listx = [1,2,3,4,5,6,7]       # 7 个元素
listy = [2,3,4,5,6,7]         # 6 个元素 
listz = [100,100,100,100]     # 4 个元素
list_result = map(lambda x,y,z : x**2 + y + z,listx, listy, listz)
print(list(list_result))
