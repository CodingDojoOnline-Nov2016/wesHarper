import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
	def setUp(self):
		#create an instance of the Underscore module
		self._ = Underscore()
		#initialize a list for testing map
		#map will apply function to every array value
		self.map_list = [1,2,3,4,5]
		self.result_map = self._.map(self.map_list, lambda x: x * 2)
		#initialize a list for testing reduce. map_list will be mutated
		self.reduce_list = [1,2,3,4,5]
		self.result_reduce = self._.reduce(self.reduce_list, lambda x,y: x + y, 10)
		#initialize list for ftesting find
		#find test should return first even value in list
		self.find_list = [1,2,3,4,5]
		self.result_find = self._.find(self.find_list, lambda x: x % 2 is 0)
		#initialize list for testing filter
		#filter result should return ALL even values
		self.filter_list = [1,2,3,4,5]
		self.result_filter = self._.filter(self.filter_list, lambda x: x % 2 is 0)
		#initialize list for testing reject
		#reject should return ALL ODD values because they will evaluate false
		self.reject_list = [1,2,3,4,5]
		self.result_reject = self._.reject(self.reject_list, lambda x: x % 2 is 0)
	def test_map(self):
		return self.assertEqual([2,4,6,8,10], self.result_map)
	def test_reduce(self):
		return self.assertEqual(25, self.result_reduce)
	def test_find(self):
		return self.assertEqual(2, self.result_find)
	def test_filter(self):
		return self.assertEqual([2,4], self.result_filter)
	def test_reject(self):
		return self.assertEqual([1,3,5], self.result_reject)

if __name__ == '__main__':
	unittest.main()