
#迭代器实现读取文本
with open('filename') as f:
    try:
        while True:
            line=next(f)
            print(line,' ')
    except StopIteration:
        pass

"""
创建一个自定义的容器对象，可以进行委托迭代，将委托请求委托到对象内部可迭代对象
"""
class Node:
    def __init__(self,value):
        self._value=value
        self._children=[]

    def __repr__(self):
        return 'Node({!r)'.format(self._value)

    def add_child(self,node):
        self._children.append(node)
#委托迭代给[]
    def __iter__(self):
        return iter(self._children)

"""
生成器模式
"""

def frange(start,stop,increment):
    x=start
    while x<stop:
        yield x
        x+=increment

"""
反向迭代
"""
#reversed方法必须作用与实现了__reversed__()特殊方法的对象，可以提前转化为list
f=open('filename')
for line in reversed(list(f)):
    print(line,' ')
#或者在自己实现的类上定义__reversed__方法
def __reversed__(self):
    n=1
    while n<=self.start:
        yield n
        n+=1

"""
itertools应用
import itertools
对迭代器进行切片
itertools.islice(c,10,20)

跳过迭代对象前一部分元素
for line in itertools.dropwhile(lamada line: line.startwith('#'),f):
    pass
或者使用切片，不过需要知道跳过多少元素， itertools.islice(c,x,none)

迭代组合
import itertools
permutations(items,k) 考虑顺序
combinations(items,k) 不考虑顺序
combinations_with_replacement(items,k) 元素可重复
k为组合元素的个数
"""


"""
enumerate(my_list,startidx)
遍历的时候，输出索引，并且可以设置起始索引
"""

"""
同时迭代多个对象
zip()
zip_longest()，会补全默认值fillvalue
对两个可迭代对象创建字典
dict(zip(a,b))
"""

"""
连续迭代多个对象，chain方法，合并容器
for x in chain(a,b):
    print(x)
    
不用多次循环和创建新的对象，减少内存
"""

"""
扁平化序列:yield from，生成加递归
from collections import Iterable

def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x
            
ignore_types的操作，避免了对字符串或者字节串，解释为可迭代对象
yield from把其他的生成器当成子例程调用等价于：
for i in faltten(x):
    yield i
"""

"""
对两个有序序列进行合并并且输出有序序列
import heapq
a,b
for c in heapq.merge(a,b):
    print(c)
"""


