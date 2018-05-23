#关键字lambda表示匿名函数，冒号前面的x表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
L = list(filter(lambda x: x%2 == 1,range(1,20)))
print(L)