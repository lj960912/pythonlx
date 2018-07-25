
'''
七段数码管---》显示日期
'''
import datetime
from turtle import *

# 每根数码管间隙
def space():
	penup()
	fd(5)
	pendown()

def draw(state):
	space()
	pendown() if state else penup()
	fd(20)
	space()
	right(90)

'''
	画七段数码管---》呈现数字
'''
def drawDigit(num):
	if num == 2 or num == 3 or num == 4 or num == 5 \
		or num == 6 or num == 8 or num == 9:
		draw(True)
	else:
		draw(False)
	draw(True) if num in (0,1,3,4,5,6,7,8,9) else draw(False)
	draw(True) if num in (2,3,5,6,8,9,0) else draw(False)
	draw(True) if num in (2,6,8,0) else draw(False)
	left(90)
	draw(True) if num in (4,5,6,7,8,9,0) else draw(False)
	draw(True) if num in (2,3,5,6,7,8,9,0) else draw(False)
	draw(True) if num in (1,2,3,4,7,8,9,0) else draw(False)
	
	penup()
	left(180)
	fd(10)
	pendown()

'''
	画日期
'''
def drawDate(date_string):
	setup(800, 300, 20, 20)
	penup()
	bk(200)
	pendown()
	pensize(5)
	speed(0)
	for s in date_string:
		if s in ("年", "月", "日"):
			penup()
			fd(5)
			pendown()
			write(s, font=("Arial", 18, "normal"))
			penup()
			fd(25)
			pendown()
		else:
			# 画数字	
			drawDigit(eval(s))

def main():
	# 获取当前日期---》格式化字符串"xxx年xxx月xxxx日"
	tstring = datetime.datetime.now().strftime("%Y年%m月%d日")
	#画日期 
九九乘法表
'''
'''
for i in range(1,10):
	for j in range(1,i+1):
		print("%d * %d = %2d" %(j, i ,j*i),end= ' ')
	print()
'''

'''

猜字游戏
'''
'''
i = 0
import random
while i < 3:
	num = int(input("输入你猜的数字:"))
	s = random.randint(1,100)
	if num == s:
		print("厉害了，500万属于你")
	elif num > s:
		print("大了，再给你一次机会")
		i += 1
		continue
	else:
		print("大胆一点")
		i += 1
		continue
print("你已经猜错三次了，下次再来吧")
'''

a = 1
i =1
sumall = (a+1)*2
while i < 9:
	sumall = (sumall+1)*2
	i+=1
print("猴子原本有{}个桃子".format(sumall))


	drawDate(tstring)	
	done()

main()

