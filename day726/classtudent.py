class Student:
	def __init__(self, name, age, scores):
		self.name = name
		self.age = age
		self.scores = scores
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
	def get_course(self):
		return max(self.scores)

stu1 = Student("赵超",22,[79,87,100])
print("姓名:{}".format(stu1.get_name()))
print("年龄:{}".format(stu1.get_age()))
print("最高分:{}".format(stu1.get_course()))

stu2 = Student("王二",22,[100,87,120])
print("姓名:{}".format(stu2.get_name()))
print("年龄:{}".format(stu2.get_age()))
print("最高分:{}".format(stu2.get_course()))
