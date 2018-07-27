class Dictclass:
	def __init__(self,dict_new):
		self.dict_new = dict_new

	#删除某个键值
	def del_dict(self,key):
		del self.dict_new[key]
		return self.dict_new
	#判断某个键是否在字典中	
	def get_dict(self,key):
		if key in self.dict_new:
			return self.dict_new[key]	
		else:
			return "not found"
	#返回键值所组成的列表
	def get_key(self):
		return self.dict_new.keys()
	#合并两个字典
	def update_dict(self,dict1):
		self.dict_new.update(dict1)
		return self.dict_new
	
dict0 = {1:'name',2:'age',3:'color'}
d = Dictclass(dict0)
print(d.del_dict(1))
print(d.get_dict(2))
print(d.get_key())
print(d.update_dict({4:'scores'}))






