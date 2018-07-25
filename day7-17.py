
m, y = eval(input("输入一个90年后的年份和日期:"))
sumdays = 0
#1990-1-1到y-m-1号有多少天
for i in range(1990,y):
	if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
		sumdays += 366
	else:
		sumdays += 365
for i in range(1,m):
	if i == 1 or i == 3 or i == 5 or \
			i == 7 or i == 8 or i == 10 or i == 12:
			sumdays += 31
	elif i == 4 or i == 6 or i == 9 or i == 11:
			sumdays += 30
	else:
			sumdays += (28 + (y % 4== 0 and y % 100 != 0 or y % 400 == 0))
sumdays += 1
week = sumdays % 7
#y，m有多少天 
if m == 1 or m == 3 or m == 5 or \
		m == 7 or m == 8 or m == 10 or m == 12:
		monthdays = 31
elif m == 4 or m == 6 or m == 9 or m == 11:
		monthdays = 30
else:
		monthdays = (28 + (y % 4== 0 and y % 100 != 0 or y % 400 == 0))
titlestr = "{}月{}".format(m,y)
print(titlestr.center(20))
print("日 一 二 三 四 五 六")
'''打印之前的空格'''
for i in range(week):
	print("   ",end='')
for d in range(1,monthdays+1):
	print("{:>2}".format(d), end= "\n" if (week+d)%7 == 0 else " ")
print()




'''
判断是否为回文数
'''


'''
num = eval(input("输入一个整型数:"))
new_num = 0
save = num
while num:
	new_num = new_num*10 + num % 10
	num //= 10
if new_num == save:
	print("{}是一个回文整型".format(save))
else:
	print("{}不是一个回文整型".format(save))

'''




'''
#判断质数
'''
'''
cnt = 0
num = range(100,1001)
for i in num:
	flag = True
	for j in range(2,i):
		if i % j == 0:
			flag = False
			break
	if flag:
		cnt += 1
print("共有{}个质数".format(cnt))

'''

'''
name = input("输入你的用户名:")
for s in name:
	if not(s.isalpha() or s.isdigit() or s == '_'):
			print("对不起，你输入的用户名无效!")
			break
else:
			print("成功读入")

		
'''		




