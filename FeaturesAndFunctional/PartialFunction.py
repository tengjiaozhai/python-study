# 偏函数
import functools

if __name__ == '__main__':
    int2 = functools.partial(int, base=2)
    print(int2('1000'))
    max2 = functools.partial(max, 10)
    print(max2(5,10,8))