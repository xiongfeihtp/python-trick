#文件读取:
import sys
sys.getdefaultencoding()

"""
文本模式，字符串，r"hello world"
"""
#'at'追加模式
with open('filename','rt',encoding='utf-8') as f:
    pass

with open('filename','rt',encoding='uft-8',errors='ignore') as f:
    pass

"""
输出重定向
with open('filename','rt') as f:
    print('hello world',file=f)
"""

"""
二进制模式'rb','wb'读写二进制数据。读取和输入的是字节串b"hello world"

二进制文件进行读取和写入的时候，需要进行解码和编码
with open('filename','rb'/'wb') as f:
    data=f.read(16)
    text=data.decode('utf-8')
    
    text='hello world'
    f.write(text.encode('utf-8'))
"""

"""
处理路径名
"""
import os
path='/Users/beazley/Data/data.csv'
os.path.basename(path)
os.path.dirname(path)
os.path.join('tmp','data',os.path.basename(path))
os.path.expanduser('~/Data/data.csv')

"""
检测文件是否存在
"""
os.path.exists(path)
"""
目录内容处理
"""
import os
fileList=os.listdir(path)
#筛选
names=[name for name in os.listdir(path) if os.path.isfile(os.path.join('somedir',name))]


"""
pickle模块，序列化python对象
"""
import pickle
data='xiongfei for machine learning'
with open('somefile','wb') as f:
    pickle.dump(data,f)

s=pickle.dumps(data)#将对象转存为字节串

with open('somefile','rb') as f:
    data=pickle.load(f)

data=pickle.loads(s)




