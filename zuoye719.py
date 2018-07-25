
'''
1.读入10个学生的成绩，要求在0~100之间，定义一个函数,
统计10个学生成绩的平均分，最高分，和最低分

2.随机产生10个10以内的整型数，存放到列表中，将列表中的最大值放在列表的最后。

3.随机产生密码：
	在26个大小写字母和10个数字组成的列表中，随机生成10个8位密码

4.定义一个列表，列表中有20个随机产生的100以内的整型数,
定义一个函数，统计20个整型数的分布情况。
每有一个数值在其所属区域打印一个*
例如5个100， 3个85,88,89
100:*****
90~99:
80~89:***
...
0~9:

def chengji(n):
	j = len(n)
	cnt = 0
	for i in n:
		cnt += i
		pingjun = cnt / j
	zuigao = max(n)
	zuidi = min(n)
	print("平均分为{},最高分为{},最低分为{}".format(pingjun, zuigao, zuidi))


s = [ eval(input("输入成绩")) for i in range(10)]
ichengji(s)

def main():
	sc = []
	i = 0
	while i < 10:
		try:
			n = int(input("请输入第{}人的成绩".format(i+1)))
			if not(0 <= n <= 100):
				print("请输入一个百分制的成绩")
				continue
		except Exception:
			print("不能是字符串")
			continue
		sc.append(n)
		i += 1
	maxValue,minValue,avgValue = opScorce(sc)
	print("最高分:"{},最低分:{},平均分:{}".format(maxValue,minValue,avdValue))

2
import random
l = [random.randint(1,9)for i in range(10)]
i = 0
while i < 10:
	j = random.randint(1,10)
	l[i] = j
	i += 1
print(l)
print(sorted(l))

'''
#3生成密码
import random
ls = []
#小写字母
for i in range(26):
	ls.append(chr(ord('a')+i))	
#大写字母
for i in range(26):
	ls.append(chr(ord('A')+i))
for i in range(20):
	ls.append(str(i))
print(ls)
for i in range(10):
	pwd = ''
	for j in range(8):
		pwd += ls[random.randint(0,61)]
	print(pwd)


'''
4统计分部情况

def fenbu(n):
	cnt = "*"
	j0 = 0
	j=0  
	j1=0	
	j2=0
	j3=0
	j4=0
	j5=0
	j6=0
	j7=0
	j8=0
	j9=0
	for i in n:
		if i //10 == 10:
			j0 += 1
		if i // 10 == 9:
			j += 1
		elif i // 10 == 8:
			j1 += 1
		elif i // 10 == 7:
			j2 += 1
		elif i // 10 == 6:
			j3 += 1
		elif i // 10 == 5:
			j4 += 1
		elif i // 10 == 4:
			j5 += 1
		elif i // 10 == 3:
			j6 += 1
		elif i // 10 == 2:
			j7 += 1
		elif i // 10 == 1:
			j8 += 1
		else:
			j9 += 1
	print("100:{}".format(j0*cnt))	
	print("90~99:{}".format(j*cnt))
	print("80~89:{}".format(j1*cnt))
	print("70~79:{}".format(j2*cnt))
	print("60~69:{}".format(j3*cnt))
	print("50~59:{}".format(j4*cnt))
	print("40~49:{}".format(j5*cnt))
	print("30~39:{}".format(j6*cnt))
	print("20~29:{}".format(j7*cnt))
	print("10~19:{}".format(j8*cnt))
	print("0~9:{}".format(j9*cnt))

import random
x = [random.randint(0,100)for i in range(20) ]
print(x)
fenbu(x)

import random
cnt = [0]*11
num =[]
for i in range(20):
	num.append(random.randint(0,100))
	cnt[num[i]//10]+= 1
print("100:",end=' ')
print(cnt[10]*"*")
for i in range(9,-1,-1):
	print("{}～{}:".format(i*10,i*10+9),end=' ')
	print(cnt[i]*"*")

'''

