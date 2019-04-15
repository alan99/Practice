"""
作者：xiaotao_1 
来源：CSDN 
原文：https://blog.csdn.net/xiaotao_1/article/details/78278622 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

def radix_sort(list, d=3): # 默认三位数，如果是四位数，则d=4，以此类推
    for i in range(d):  # d轮排序
        s = [[] for k in range(10)]  # 因每一位数字都是0~9，建10个桶
        for j in list:
            s[int(j / (10 ** i)) % 10].append(j)  
        re = [a for b in s for a in b]
    return re

L = [120,230,222,512,991,231,540,320,444]
print(radix_sort(L))

L = [1202,3230,2522,5612,9491,2331,5240,3620,4454]
print(radix_sort(L,4))
