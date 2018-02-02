#类和对象的
class Data:
    __slots__ = ['year','month','day']
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
"""
创建大量实例的时候，减少对内存的使用
"""
