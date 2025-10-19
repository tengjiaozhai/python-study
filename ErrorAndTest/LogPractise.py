# 错误 和 日志的练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce
import logging
def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        logging.error(e)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
