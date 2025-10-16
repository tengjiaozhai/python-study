# 迭代
def findMinAndMax(L):
    length = len(L)
    for item in range(length):
        swap = False
        for i in range(length - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                swap = True
        if not swap:
            break
    if length > 0:
        return (L[0], L[length - 1])
    else:
        return (None, None)


if __name__ == '__main__':
    # 测试:
    if findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
