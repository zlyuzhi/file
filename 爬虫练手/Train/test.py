# import random
# teacher_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# office_list = [[], [], []]
# for i in range(len(teacher_list)):
# 	teacher = random.choice(teacher_list)
# 	office_id = random.randint(0,len(office_list)-1)
# 	if len(office_list[office_id]) < 3:
# 		office_list[office_id].append(teacher)
# 		teacher_list.remove(teacher)
# print(office_list)
	
# class A(object):
# 	def a(self):
# 		print(self.num)

# 	def b(self):
# 		self.num = 3
# 		self.a()

# a = A()
# a.b()
import re
lists = ['http://news.sina.com.cn',
		 'http://autofgfd.sina.com.cn']

for each in lists:
	ret = re.findall("//(.+?)\.", each)[0]
	print(ret)
	# print(ret.group(1))
	print('*' * 30)



