'''
def pinfang(n):
	n = n **2
	return n
def maxz(s):
	m = s[0]
	length = len(s)
	for i in range(1,length):
		if s[i] > m:
			m = s[i]
	return m
#求整数的平方

j = 0
while j< 5:
	num = int(input("输入一个整型数:"))
	print( pinfang(num))
	j += 1

s = input("输入一个字符串:")
print(maxz(s))



def max_yue(m,n):
	while True:
		t = m % n
		if t == 0:
			break
		#没整除
		m = n
		n = t
	return n

#默认参数
def sumn(n,m=2):
	n = n**m
	return n
print(sumn(10))
print(sumn(10,3))


#统计所有形参的和

#可变参数

def sumall(*arg):
	s = 0
	for i in arg:
		#print (i)

		s += i
	print(s)


对字符串进行逆序
'''
def nixu(n):
	if n == "":
		return n 
	return nixu(n[1:])+ n[0]


s= input("输入一个字符串:")
print(nixu(s))


