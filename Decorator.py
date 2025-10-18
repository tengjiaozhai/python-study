# 装饰器
import functools
import time
from curses import wrapper

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def metric(fn):
    start = time.time()
    print('%s executed start %s ms' % (fn.__name__, start))
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        # 调用原函数
        return fn(*args, **kw)
    end = time.time()
    print('%s executed in %s ms' % (fn.__name__, end-start))
    return wrapper

if __name__ == '__main__':
    print(is_palindrome(10))
    # 测试
    @metric
    def fast(x, y):
        time.sleep(0.0012)
        return x + y;


    @metric
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z;


    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')