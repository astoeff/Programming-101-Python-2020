import unittest
import json


class Panda(WithAttributes, WithEqualAttributes, Jsonable):
	pass

class Car(WithAttributes, WithEqualAttributes, Jsonable):
	pass

class TestJasonable(unittest.TestCase):
	def test_to_json_should_return_empty_json_for_objects_with_no_arguments(self):
		panda = Panda()

		result= panda.to_json(indent=4)
		expected = {'type' : Panda.__name__,
					'dict' : {}}

		self.assertEqual(result, json.dumps(expected,indent=4))

	def test_to_json_should_return_correct_json_with_arguments(self):
			panda = Panda(name='Marto', age=20, weight=100.10)

			result= panda.to_json(indent=4)
			expected = {'type' : Panda.__name__,
						'dict' : {
								  'name' : 'Marto',
								  'age' : 20,
								  'weigth' : 100.10
						}}



			self.assertEqual(result, json.dumps(expected,indent=4))

def test_to_json_should_return_correct_json_with_nested_arguments(self):
			oanda = Panda(food=['bamboo', 'grass'], skills = {'eat' : 100, 'sleep' : 200})
			panda = Panda(name='Marto', age=20, weight=100.10)

			result= panda.to_json(indent=4)
			expected = {'type' : Panda.__name__,
						'dict' : {
								  'name' : 'Marto',
								  'age' : 20,
								  'weigth' : 100.10
						}}



			self.assertEqual(result, json.dumps(expected,indent=4))

def test_with_complex_object(self):
	panda = Panda(name='MArto', friend=Panda('Ivo'))
	

def test_from_json_with_no_arguments(self):
	panda = Panda()
	panda_json = panda.to_json()

	result = Panda.from_json(panda_json)

	self.assertEqual(panda, result)

def test_from_json_with_wrong_class_type(self):
	panda = Panda()
	car = Car()
	panda_json = panda.to_json()

	result = Panda.from_json(car.to_json())
	# trqa grumne

	self.assertEqual(panda, result)

def test_from_json_with_arguments(self):
	panda = Panda('name', 'age')
	panda_json = panda.to_json()

	result = Panda.from_json(panda.to_json)
	# trqa grumne

	self.assertEqual(panda, result)

if __name__ == '__main__':
	unittest.main()