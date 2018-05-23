h = 1.79
w = 70.4
BMI = w/pow(h,2)
if BMI<18.5:
    print('BMI指标为', BMI, '，结果表示体重过轻')
elif BMI<=25:
    print('BMI指标为', BMI, '，结果表示体重正常')
elif BMI<=28:
    print('BMI指标为', BMI, '，结果表示体重过重')
elif BMI<=32:
    print('BMI指标为', BMI, '，结果表示身体肥胖')
else:
    print('BMI指标为', BMI, '，结果表示身体严重肥胖')