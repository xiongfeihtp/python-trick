import sys
import csv

def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
            pass

if __name__=='__main__':
    main(sys.argv[1])

"""
写入函数，创建的局部变量，程序会运行的更快，局部变量比全局变量更快
"""
