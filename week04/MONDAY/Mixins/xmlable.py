#This version works correctly with noon-nested objects
# import xml.etree.ElementTree as ET

# class Xmlable:
# 	def to_xml(self):
# 		root = ET.Element(self.__class__.__name__)
# 		for el in self.__dict__:
# 			sub_el = ET.SubElement(root, str(el))
# 			sub_el.text=str(self.__dict__[el])
# 		return ET.tostring(root)

# class Panda(Xmlable):
# 	def __init__(self, name):
# 		self.__name = name

# class Person(Xmlable):
# 	def __init__(self, name, panda):
# 		self.__name = name
# 		self.panda = panda

# if __name__ == '__main__':
# 	panda = Panda('gosho')
# 	# print(panda.to_xml())

# 	person = Person('antoni', 25)
# 	print(person.to_xml())

import xml.etree.ElementTree as ET
from mixins import WithSetAttributes
from mixins import WithEqualAttributes

class Xmlable:
	def is_primitive(obj):
		return not hasattr(obj, '__dict__')

	def to_xml(self):
		root = ET.Element(self.__class__.__name__)
		for el in self.__dict__:
			if not Xmlable.is_primitive(self.__dict__[el]):
				sub_el = ET.SubElement(root, str(self.__dict__[el]))
				el_text = self.__dict__[el].to_xml()
				el_text = str(el_text)[2:len(str(el_text))-1]
				el_text = el_text.replace("&gt;", ">")
				el_text = el_text.replace("&lt;", "<")

				# print(str(el_text))
				# sub_el.text = el_text.replace("&gt;", ">").replace("&lt", "<")
				sub_el.text = el_text
				# print(sub_el.text)
				# s = s.replace("&gt;",">")
 # s = s.replace("&lt;","<")
			else:
				sub_el = ET.SubElement(root, str(el))
				sub_el.text=str(self.__dict__[el])
				text = ET.tostring(root)
				# text = text.replace("&gt;", ">")
				# text = text.replace("&lt;", "<")
				# print(text)
		return text


	@classmethod
	def from_xml(cls, xml_string):
		root = ET.fromstring(xml_string)
		# print(xml_string)
		class_name = root.tag
		# print(class_name)
		# print(cls.__name__)
		if class_name != cls.__name__:
			raise ValueError('err')
		
		attributes = {}
		for child in root.iter():
			# print(child.tag, ':' ,child.attrib)


			if child.text != None:
				attributes[child.tag] = child.text
			# print()
			# print(dir(child))

			# print(dir(child))
				# print('tuk')

		return cls(**attributes)

		
# root = tree.getroot()

# # changing a field text
# for elem in root.iter('item'):
#     elem.text = 'new text'

# # modifying an attribute
# for elem in root.iter('item'):
#     elem.set('name', 'newitem')

# # adding an attribute
# for elem in root.iter('item'):
#     elem.set('name2', 'newitem2')

# tree.write('newitems.xml')


# 		data = json.loads(json_string)

# 		class_name = data['type']
# 		attributes = data['dict']

# 		if class_name != cls.__class__.__name__:
# 			raise ValueError('err')

# 		return cls(**attributes)


# class WithSetAttributes:
# 	def __init(self, **kwargs):
# 		for name, value in kwargs.items():
# 			setattr(self, name, value)

class Panda(Xmlable):
	# def __init__(self, name, age):
	# 	self.__name = name
	# 	self.__age = age

	# def __repr__(self):
	# 	return self.__class__.__name__
	def __init__(self, **kwargs):
		for name, value in kwargs.items():
			setattr(self, name, value)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	pass

class Car(Xmlable):
	def __init__(self, color):
		self.__color = color

class Person(Xmlable):
	def __init__(self, name, panda):
		self.__name = name
		self.panda = panda

if __name__ == '__main__':
	panda = Panda(name='gosho', age=25)
	# car = Car('red')
	# print(panda.to_xml())

	# person = Person('antoni', panda)
	# # person.to_xml()
	# print(person.to_xml())
	xml_string = panda.to_xml()
	# # car_2 = Car.from_xml(xml_string) 
	panda_2 = Panda.from_xml(xml_string)
	print(xml_string)
	print(panda_2.__dict__)
	print(panda.__dict__)
	# assert panda == panda_2 ,'{p1} != {p2}'.format(p1=panda, p2=panda_2)

