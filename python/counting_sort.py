"""
作者：xiaotao_1 
来源：CSDN 
原文：https://blog.csdn.net/xiaotao_1/article/details/78278622 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
def counting_sort(a, k):  # k = max(a)
    n = len(a)          # 计算a序列的长度
    b = [0] * n         # 设置输出序列并初始化为0
    c = [0] * (k+1)     # 设置计数序列并初始化为0，
    
    for j in a:         # 計次
        c[j] += 1
    
    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    for j in a:
        b[c[j] - 1] = j
        c[j] -= 1
    
    return b

L = [2,1,0,4,2,6,2,1,1,4,5]
print(counting_sort(L, max(L)))
