'''
j= 0
s=input("输入一个字符串:")
for i in s:
	if ord('a') <= ord(i) <= ord('z'):
		print(chr(ord(i) - (ord('a')-ord('A'))))
	elif ord('A') <= ord(i) <= ord('Z'):
		print(chr(ord(i) + (ord('a') - ord('A'))))
		



输入数，判断大小

num1 = int(input("输入数:"))
num2 = int(input("输入数:"))
if num1 < num2:
	print("num1小于num2")
elif num1 ==num2:
	print("num1等于num2")
else:
	print("num1大于num2")


#比较字符串大小，只跟第一个不相同的字符大小有关

str1 = input("输入一个字符串:")
str2 = input("输入字符串:")
i = 0
j = 0
while i <= len(str1) and j <= len(str2):
	if ord(str1[i]) < ord(str2[j]):
		print("str1 小于str2")
		break
	elif ord(str1[i]) > ord(str2[j]):
		print("str1 大于str2")
		break
	i += 1
	j += 1


str3 = input("输入字符串:")
digit_cnt = 0
lower_cnt = 0
upper_cnt = 0
for i in str3:
	if i.isupper():
		upper_cnt += 1
	elif i.islower():
		lower_cnt += 1
	elif i.isdigit():
		digit_cnt += 1
print("字符串中共有{}个大写字母，{}个小写字母，{}个数字".format(upper_cnt,lower_cnt,digit_cnt))


s = input("输入一个字符串:")
#print(s.title())
i = 0
flag = True
while i < len(s):
	if ord('A')<= ord(s[i])<= ord('Z') or ord('a') <= ord(s[i]) <= ord('z'):
		if flag:#首字母
			print(s[i].upper(), end='')
			flag = False
		else:
			print(s[i].lower(), end='')
	elif s[i] == ' ':
		flag = True
		print(s[i], end='')
	else:
		print(s[i], end='')
	i += 1
print() 

'''

'''
import time
def testhello():
	print("hello")

if __name__ == "__mian__":
	print(dir(time))
	print(__name__)
	print("this is myself file")
testhello()
'''
'''
import sys
def add2num(num1,num2):
	return num1 + num2
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("参数不够")
	else:
		print(add2num(int(sys.argv[1]), int(sys.argv[2])))


'''



fd = open("725","w+")
'''
#print(fd.read())
fd.write("boy  \ngirle\n")
print("当前文件的偏移量:{}".format(fd.seek(6,0)))

r = fd.read()
print(r)
fd.close()



with open("724","a") as f:
	print(f.tell())
'''









