'''
l =[1,2,3,4,5,4,6,7]
print(l.index(4,3,-1))

print(l.count(4))
'''

def text(num, ls=[]):
	ls.append(num)
	return ls

l1= text(12)
l2= text(123, ["hekki"])
l3= text("a")

print(l1)
print(l2)
print(l3)


#列表生成式
a1 = [i*i for i in range(1,11)]
print(a1)
a2 = [i*i for i in range(1,11) if i % 2]
print(a2)





