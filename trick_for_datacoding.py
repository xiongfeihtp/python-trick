"""
def function_with_one_star(*t):
    print(t, type(t))

def function_with_two_stars(**d)
    print(d, type(d))


上面定义了两个函数，分别用了带一个星号和两个星号的参数，它们是什么意思，运行下面的代码：

function_with_one_star(1, 2, 3)
function_with_two_stars(a=1, b=2, c=3)
结果如下

(1, 2, 3) <


class 'tuple'>


{'a': 1, 'c': 3, 'b': 2} <


class 'dict'>


由此可见，带一个星号（ * ）参数的函数传人的参数存储为一个元组（tuple）；

而带两个星号（ * ）参数的函数传人的参数则存储为一个字典（dict），并且在

调用是采取
a = 1, b = 2, c = 3
的形式。

由于传人的参数个数不定，所以当与普通参数一同使用时，必须把带星号的参数放在最后。
"""

"""
csv json

json和pickle用法一致：包括loads dumps load dump，并且支持的数据格式繁多，如果涉及到深层次的结构需要打印，
可以采用：
from pprint import pprint
pprint(data) #可以打印多层信息
"""

"""
json对读取的数据结构进行预处理
"""
from collections import OrderedDict
import json
s='dasdasd'
data=json.loads(s,object_hook=OrderedDict)


"""
在任何涉及统计，时间序列的数据分析问题时，最好使用pandas
"""
import pandas as pd



