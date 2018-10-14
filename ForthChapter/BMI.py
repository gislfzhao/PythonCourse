# BMI
height, weight = eval(input())
bmi = weight / pow(height, 2)
print("BMI数值：{:.2f}".format(bmi))
nat, dom = "", ""
if bmi < 18.5:
    nat, dom = "偏瘦", "偏瘦"
elif bmi < 24:
    nat, dom = "正常", "正常"
elif bmi < 25:
    nat, dom = "正常", "偏胖"
elif bmi < 28:
    nat, dom = "偏胖", "偏胖"
elif bmi < 30:
    nat, dom = "偏胖", "肥胖"
else:
    nat, dom = "肥胖", "肥胖"
print("BMI指标为:国际'{}', 国内'{}'".format(nat, dom))
