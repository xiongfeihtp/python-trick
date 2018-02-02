"""
数学结构与算法
"""

import heapq
#heapq模块：对堆得利用
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        #index维护优先相同的元素的次序
        self._index=0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index+=1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


#元组比较原则
"""
A=(a,b,c)
B=(e,d,f)
A和B的比较是按照顺序比较的。如果递归到某一项无法比较，则会报错，所以可以安排辅助参数如上面的index，来帮助排序
"""

"""
使用zip可以将字典的键和值进行反转，从而可以对元组元素进行排序
min_price=min(zip(prices.values(),prices.keys())
但是需要注意的是，zip创建的是一个迭代器，内容只能被消耗一次
"""

"""
对字典的特定键或者类的属性进行选定，从而对字典和类进行排序
key=itemgetter attrgetter lamada x:...都可以，前两种更加快速。
"""

"""
groupby +key=...对指定维度进行分组，并且返回一个value和子迭代器
"""
A=[1,4,-5,4,1,34,4]
[n if n>0 else 0 for n in A]
B=[1,'N/A','-',5]
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False
ivals=list(filter(is_int,B))

"""
列表推导式
生成推导式
字典推导式

{key:value for key,value in prices.items() if key in tech_name}
相比于dict((key,value) for key,value in prices.items() if value>200)速度更快
"""
"""
ChainMap合并两个映射，并且不需要创建新的字典，并且直接修改可以直接反应到原字典上。
"""


"""
字符串和文本
"""

"""
1，字符串的分割，split只能完成简单的工作，只支持单分隔符，re.split可以支持多分隔符
"""
import re
line='asdf ,fjdk;afed,     fijek:dsad,   da'
A=re.split(r'[,:;\s]\s*',line)
'x'.join(A)


"""
文本查找
re.finditer() 迭代输出
re.findall()  找出所有
re.match()  找出一个，从开头开始
re.compile(r'(\d+)/(\d+)/(\d+)')
"""

"""
文本替换
replace
re.sub('(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
newtext,n=re.subn() 同时返回替换的次数
"""
"""
re模块不区分大小写的话，只需要加上flags=re.IGNORECASE
但是匹配出来的新文本大小写与原文本不匹配

最短匹配(.*?)
"""

"""
1,(.*)不能匹配换行符
如果需要对文本块进行匹配，则需要添加对换行符的支持
re.compile(r'/\*((?:.|\n)*?)\*/')
其中(?:.|\n)只做匹配，不捕获结果
2,compile()中的属性re.DOTALL可以使.匹配所有字符，包括换行符
"""

"""
unicode的统一表示规范
import unicodedata
t1=unicodedata.normalize('NFC',s1)
"""

"""
s.strip
s.lstrip
s.rstrip
with open(filename) as f:
    lines=(line.strip() for line in f)
    for line in lines:
        pass
"""

"""
文本清理和过滤
str.upper() str.lower()
str.replace re.sub()
unicodedata.normalize()

清理整个范围内的字符
remap是一个小型的转换表
translate(remap)
其实str.replace是最快的方法
"""

"""
对齐文本字符串
ljust()
rjust()
center()
"""


"""
字符串连接
+和join相比，效率低的多
小技巧
','.join(str(d) for d in data)
"""

"""
格式化文本
import textwrap
textwrap.fill(s,70)
以固定的列数，显示文本
就是重新加\n
"""


"""
python中的随机
import random
random.choice
random.sample(values,n)
random.shuffle(values)
random.randint(0,10)
random.random() 0到1之间的均匀分布
random.getrandbits() 随机比特
random.sedd()

random.uniform
random.gauss

random模块不应该应用于加密处理程序中，应该使用ssl模块中的函数替代
"""

