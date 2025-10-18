# 匿名函数
def is_odd(n):
    return n % 2 == 1

if __name__ == '__main__':
    L = list(filter(lambda x:x % 2 == 1, range(1, 20)))
    print(L)
