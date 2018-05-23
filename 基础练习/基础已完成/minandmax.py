def findMinAndMax(L):
    Min = None
    Max = None
    for n in L:
        if Min == None:
            Min = n
        elif n < Min:
            Min = n
        if Max == None:
            Max = n
        elif n > Max:
            Max = n
    return(Min, Max)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')