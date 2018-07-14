j= 0
s=input("输入一个字符串:")
for i in s:
	if ord('a') <= ord(i) <= ord('z'):
		print(chr(ord(i) - (ord('a')-ord('A'))))
	elif ord('A') <= ord(i) <= ord('Z'):
		print(chr(ord(i) + (ord('a') - ord('A'))))
		
