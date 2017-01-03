class Underscore(object):
	#map creates a new list with each item transformed by the callback
	def map(self, array, callback):
		for i in range(len(array)):
			array[i] = callback(array[i])
		return array
	#reduce takes an array, a starting value, and a callback
	#reduce applies the callback to each value and the combined return value of each
	#consecutive transformation to return a single value
	#ex: reduce([1,2,3,4], lambda x,y: x+y, 10) returns 20 or ((((10+1)+2)+3)+4)
	def reduce(self, array, callback, initial):
		for num in array:
			initial = callback(initial, num)
		return initial
	#find finds the value which produces the first truthy instance when run through callback
	#given an array
	def find(self, array, callback):
		for i in range(len(array)):
			if callback(array[i]):
				return array[i]
		return None
	#filter is the same as find but returns all instances that evaluate truthy in a new array
	def filter(self, array, callback):
		result = []
		for i in range(len(array)):
			if callback(array[i]):
				result.append(array[i])
		return result
	#reject is the exact opposite of filter, used for instances that evaluate falsey
	def reject(self, array, callback):
		result = []
		for i in range(len(array)):
			if not callback(array[i]):
				result.append(array[i])
		return result

# _ = Underscore()
# print _.map([1,2,3,4], lambda x: x ** 2)

# print _.reduce([1,2,3,4,5], lambda x,y: x+y, 15)

# even = _.find([1,1,3,5,5,8], lambda x: x % 2 is 0)
# print even

# evens = _.filter([1,2,3,4,5,6], lambda x: x % 2 is 0)
# print evens

# not_evens = _.reject([1,2,3,4,5,6], lambda x: x % 2 is 0)
# print not_evens