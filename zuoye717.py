'''
BMI
'''

height, weight = eval(input("兄弟，多高多重啊!:"))
bmi = height/(weight**2)
print(bmi)
if bmi < 18.5:
	print("多吃点吧，太瘦了")
elif 18.5 <= bmi <= 23.9 :
	print("完美！不用减肥了")
elif 24 <= bmi <= 27:
	print("过重") 
elif 28 <= bmi <= 32:
	print("肥胖,要考虑减肥了")
else:
	print("不能再胖了")


'''
计算前N项和
'''
n = eval(input("输入一个数字:"))
sumall = 0
for i in range(1,n+1):
	sumall += i
print("{}的前n项和是{}".format(n,sumall))















