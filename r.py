from sys import argv

print('命令行参数',argv, sep=':') # argv是接收命令行的参数, list类型

# 读取文件内容， 参数是第2个，索引位置是1
if len(argv) == 1: raise Exception('未指定文件名')

fileName = argv[1]

with open(fileName, encoding='utf-8') as f:
     print(''.join(f.readlines()), end='')  # 读取文本文件中的所有行数据


