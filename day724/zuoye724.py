'''
import sys
def mycp(file1,file2,file3):
	fd = open(file1)
	fd1 = open(file2,"w+")
	cnt = 0
	while True:
		retxt = fd.readline()
		cnt+=1
		if retxt=="":
			break
		fd1.write(retxt)
		if cnt == 2:
			fd1.write(file3)
	fd.close()
	fd1.close()
def main():
	if not(len(sys.argv) >= 4):
		print("至少需要3个参数")
	else:
		mycp(sys.argv[1],sys.argv[2],sys.argv[3])



main()
'''
'''
import sys

def bijiao(file1,file2):
	fd = open(file1)
	fd1 = open(file2)
	cnt = 1
	while True:
		etxte = fd.readline()
		etxte1 = fd1.readline()
		if etxte != etxte1:
			print("第{}行不同".format(cnt))
			cnt+=1
		else:
			cnt += 1
		if etxte=="" or etxte1=="":
			break
			
def main():
	if not(len(sys.argv >= 3)):
		print("至少需要两个文件")
	else:
		bijiao(sys.argv[1],sys.argv[2])

main()
'''	
import sys
def dayin(file,n):
	i = 0
	while True:
		fd = open(file)
		etxte = fd.readlines()
		if i < int(n):
			print(etxte[i])
			i += 1
		else:
			fd.close()
			break
def main():
	if not(len(sys.argv) >= 3):
		print("需输入至少两个参数")
	else:
		dayin(sys.argv[1],sys.argv[2])

main()
		


