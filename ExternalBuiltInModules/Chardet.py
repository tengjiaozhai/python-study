#字符编码 转换
import chardet

print(chardet.detect(b'Hello, world!'))
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))