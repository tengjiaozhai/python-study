# 函数 map 和 reduce
from functools import reduce


def fn(x,y):
    return x * 10 + y
def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]
# 首字母大写
def normalize(name):
    return name[0].upper() + name[1:]
# sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    gtZero = s.split('.')[0]
    lgZero = s.split('.')[1]
    gt = reduce(lambda x, y: x * 10 + y, map(char2nums, gtZero))
    lg = reduce(lambda x, y: x *0.1 + y, map(char2nums, lgZero[::-1]))
    return gt+lg*0.1
def char2nums(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

if __name__ == '__main__':
    print(reduce(fn, map(char2num, '13579')))
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')