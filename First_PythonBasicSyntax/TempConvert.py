# # TempConvert.py
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0: -1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0: -1]) + 32
    print("转化后的温度是{:.2f}F".format(F))
else:
    print("输入格式有错误")

# TempConvert.py
TempStr = input("请输入带有符号的温度值(例：F15, f14.2, C34, c23)：")
if TempStr[0] in ['F', 'f']:
    C = (eval(TempStr[1:]) - 32) / 1.8
    print("转换后的温度是{:.4f}C".format(C))
elif TempStr[0] in ['C', 'c']:
    F = 1.8 * eval(TempStr[1:]) + 32
    print("转化后的温度是{:.4f}F".format(F))
else:
    print("输入格式有错误")
