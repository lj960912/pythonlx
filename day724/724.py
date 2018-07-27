import os
if os.path.exists("/home/liangjun/pythonlx/666.py"):
	print("1")
else:
	print("0")

if os.path.isfile("/home/liangjun/pythonlx/666.py"):
	print("是")
else:
	print("否")


print(os.path.join("/etc/", "passwd"))
print(os.path.split("/home/liangjun/pythonlx/666.py"))
print(os.stat("666.py"))
print(os.listdir("/home/liangjun/pythonlx/"))

if os.path.exists("/home/liangjun/pythonlx/day7-19.py"):
	print("存在")
else:
	print("不存在")

if os.path.isfile("/home/liangjun/pythonlx/day7-18.py"):
	print("{}是普通文件".format("/home/liangjun/pythonlx/666.py"))
else:
	print("不是一个普通文件")

