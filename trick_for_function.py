#函数的参数
def avg(first,*rest):
    return (first+sum(rest))/(1+len(rest))

def anyargs(*args,**kwargs):
    print(args)
    print(kwargs)

"""
*表示任何参数，输入是以元组形式
**表示关键字参数，输入的是以字典的形式

*只能作为最后一个位置参数，**只能作为最后一个参数
"""

"""
内联式函数
add=lamada x,y:x+y
add(2,3)
add('hello','world')

sorted(names,key=lamada name:name.split()[-1].lower())
"""

