# 切片
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    if name == 18:
        print("调用空函数")
        pass
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[-1])
    print((0, 1, 2, 3, 4, 5)[:3])

def trim(s):
    i = 0
    j = 0
    for c in s:
        if c == ' ':
            i += 1
        else:
            break
    for c in reversed(s):
        if c == ' ':
            j += 1
        else:
            break
    print(s[i:len(s) - j])
    print(s.strip())
    return s[i:len(s) - j]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 测试:
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
