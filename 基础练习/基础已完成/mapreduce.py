from functools import reduce

CHAR_TO_FLOAT={
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '.':-1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch],s) #ch指的是参数，map(func, 参数)，func = lambda ch: CHAR_TO_FLOAT[ch]
    point = 0
    print(list(nums))
    def to_float(f,n):
        print(f,n)
        nonlocal point
        if n == -1:  #当遇到'.'时，对应为-1，这时将point的值改为1，使后面计算小数点后的值（即第三步else）
            point = 1
            return f
        if point == 0:  #如果没遇到'.'，则按正常整数计算方法返回值
            return f*10+n
        else:
            point = point*10
            return f+n/point
    return reduce(to_float,nums,0.0) #reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4),第三个参数是初始值，第一步用初始值和序列中的第一个值代入函数进行计算

print(str2float('.1234'))