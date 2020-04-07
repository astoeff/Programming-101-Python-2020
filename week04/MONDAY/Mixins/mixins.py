import json

class WithEqualAttributes:
	def __eq__(self, other):
		return self.__dict__ == other.__dict__

class WithSetAttributes:
	def __init(self, **kwargs):
		for name, value in kwargs.items():
			setattr(self, name, value)

class Xmlable:
	def to_xml(self):
		name = self.__class__.__name__
		return name

class Jsonable:
	def is_primitive(obj):
		return not hasattr(obj, '__dict__')

	# def f(obj):
	# 	if Jsonable.isPrimitive(obj):
	# 		return obj
	# 	return obj.to_json()


	@classmethod
	def from_json(cls, json_string):
		data = json.loads(json_string)

		class_name = data['type']
		attributes = data['dict']

		if class_name != cls.__class__.__name__:
			raise ValueError('err')

		return cls(**attributes)

	def to_json(self, indent = 4):
			name = self.__class__.__name__

			attributes = {}
			for el in self.__dict__:
				# print(el,':')
				if not Jsonable.is_primitive(self.__dict__[el]):
					attributes[el] = str(json.dumps(self.__dict__[el].to_json()))
					for sth in (self.__dict__[el].__dict__):
						print(sth, ':', self.__dict__[el].__dict__[sth])
				else:
					attributes[el] = self.__dict__[el]
					# print(self.__dict__[el])

			return json.dumps({'type' : name, 'dict' : attributes},indent=indent)
		# # list_of_repr = [el.__dict__ for el in self.__dict__]
		# # dictionary_of_els = {}
		# # for el in list_of_repr:
		# # 	dictionary_of_els[el] = self.__dict__[el]


		# object_json = json.dumps(self.__dict__, default=lambda o:Jsonable.f(o) , indent=indent)
		# print(object_json)
		# dictionary = {'type' : self.__repr__(), 'dict' : object_json}
		# # return json.dumps(dictionary, indent=indent)
		#  # + json.dumps(, indent=indent)
		# return json.dumps(dictionary, indent=indent)
		# # default=lambda o: o.to_json() if Jsonable.isPrimitive(o) else o


		# bachka
		# return json.dumps(self.__dict__, default=lambda o:Jsonable.f(o) , indent=indent)
class Panda(Jsonable, Xmlable, WithSetAttributes):
	# def __init__(self, name):
	# 	self.__name = name

	# def __repr__(self):
	# 	return 'Panda'
	pass


class Person(Jsonable):
	def __init__(self, name, panda):
		self.__name = name
		self.panda = panda

# class Human(Jsonable):
#  	def __init__(self, name, age):
#  		self.name = name
#  		self.age = age

#  	def __repr__(self):
#  		return 'Human'

#  	def __str__(self):
#  		return 'Human'


# h = Human('Joro', 24)
# # print(h.__repr__())
# # print(dir(h))
# print(h.to_json())

# person = Person('Pesho', panda=Panda('Marto'))
# print(person.to_json(indent = 2))

# print('============================================================')

# panda = Panda('gosho')
# print(panda.to_json())

# panda = Panda(name='gosho')
# print(panda.to_xml())

# import json 
# from typing import List
# class Student(object):
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
# class Team(object):
#     def __init__(self, students: List[Student]):
#         self.students = students        
# student1 = Student(first_name="Jake", last_name="Doyle")
# student2 = Student(first_name="Jason", last_name="Durkin")
# team = Team(students=[student1, student2])

# json_data = json.dumps(team, default=lambda o: o.__dict__, indent=4)
# print(json_data)