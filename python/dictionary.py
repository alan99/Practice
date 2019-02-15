dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
 
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
 
# 输出结果
print(dict1)
print(dict2)
print(dict3)

########################

print(dict1['user'])
print(dict1.get('user', 'not'))

x = dict1.get('sex', 'not') + 'm'
print(x)
print('user' in dict1)
print('sex' in dict1)

dict1.setdefault('sex', 'm')
print('sex' in dict1)
print(dict1['sex'])

print(dict1)
print(dict2)
print(dict3)

dict1['age'] = dict1.get('age', 20) + 1
print(dict1['age'])