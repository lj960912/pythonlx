'''

模拟进度条
'''

import time
i = 0
scale = 10
print("开始下载".center(20,'-')) #将给定字符串居中，占20宽度，不够补"-"
while i <= scale:
	js = i*'##'
	ws = (scale-i) * '--'
	'''
	python中的转义字符
			\n换行
			\tTab制表符
			\r回车
			\b退格

	'''
	print("\r{:^3.0f}%[{}{}]\" \\ \ta\bb".format(i/scale*100,js,ws),end='')
	i += 1
	time.sleep(0.5) #延时0.5秒
print()
print("下载完成".center(20,'-')) #




'''
判段空气质量：
'''
pmzhi =int(input("输入今天的pm2.5值:"))
if pmzhi > 75:
	print("今天是重度污染，不易出门")
elif 35 < pmzhi <= 75:
	print("空气良好，可以进行适当户外活动")
else:
	print("出来嗨")
print("空气{}污染" .format("是" if pmzhi > 75 else "没有"))





