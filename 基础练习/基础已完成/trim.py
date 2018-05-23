def trim(n):
    if n == '' or (n[0] !=' ' and n[-1] != ' '):
        return n
    elif n[0] == ' ':
        print(n[1:])
        trim(n[1:])
    elif n[-1] == ' ':
        print(n[:-1])
        trim(n[:-1])

if trim('hello  ') != 'hello':
    print('1测试失败')
elif trim('  hello') != 'hello':
    print('2测试失败')
elif trim('  hello world  ') != 'hello world':
    print('3测试失败')
elif trim('') != '':
    print('4测试失败')
elif trim('    ') != '':
    print('5测试失败')
else:
    print('测试成功')
