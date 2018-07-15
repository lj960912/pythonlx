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


'''
#比较字符串大小，只跟第一个不相同的字符大小有关
'''
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
'''

s = input("输入一个字符串:")
s1 = s.split( ) 
while i < len(s1):
	
	s2 = s1[i] 

	j = 1
	i += 1
	while j < len(s2):
		j += 1
		if ord('a') <= ord(s2[0])<= ord('z') 
			ord(s2[0]) = ord(s2[0]) - (ord('a') - ord('A')) 
		elif ord('A') <= ord(s2[j]) <= ord('Z'):
			chr(ord(s2[j])) = chr(ord(s2[j]) + (ord('a') - ord('A')))

print(s2)












s= "boy,fdf yj r4,hr    fg"
print(s.split( ))

