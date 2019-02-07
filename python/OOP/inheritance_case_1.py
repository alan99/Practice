class Ironmen:
    '''這是一個叫做 Ironmen 的類別''' # Doc string
    def __init__(self, group, participants):
        self.group = group
        self.participants = participants
    
    def print_info(self):
        print(self.group, "組有", self.participants, "位鐵人參賽！")

# Articles 類別繼承 Ironmen 類別
class Articles(Ironmen):
    '''
    這是一個叫做 Articles 的類別。
    Articles 繼承 Ironmen 類別，她新增了一個 print_articles() 方法
    '''
    def print_articles(self):
        print(self.group, "組預計會有", self.participants * 30, "篇文章！")

# 根據 Articles 類別建立一個物件 modern_web
modern_web = Articles("Modern Web", 54)

# 使用 modern_web 的 print_articles() 方法
modern_web.print_articles()

# 檢查 modern_web 是否還擁有 print_info() 方法
modern_web.print_info()