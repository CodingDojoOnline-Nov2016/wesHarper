#This works only with one dimensional lists and tuples
#isinstance works better than type when evaluating subclasses
#"if type(item) is list": evaluated true when type(item) == int because it doesn't play nice with subclasses

class MathDojo(object):
	def __init__(self):
		self.result = float(0)
	def add(self, val, *more_vals):
		if isinstance(val, list) or isinstance(val, tuple):
			for num in val:
				self.result += float(num)
		elif isinstance(val, int) or isinstance(val, float):
			self.result += float(val)
		for item in more_vals:
			if isinstance(item, list) or isinstance(item, tuple):
				for num in item:
					self.result += float(num)
			elif isinstance(item, int) or isinstance(item, float):
				self.result += float(item)
		return self
	def subtract(self, val, *more_vals):
		if isinstance(val, list) or isinstance(val, tuple):
			for num in val:
				self.result -= float(num)
		elif isinstance(val, int) or isinstance(val, float):
			self.result -= float(val)
		for item in more_vals:
			if isinstance(item, list) or isinstance(item, tuple):
				for num in item:
					self.result -= float(num)
			elif isinstance(item, int) or isinstance(item, float):
				self.result -= float(item)
		return self

md = MathDojo()
# print md.add(2).add(2, 5).subtract(3, 2).result
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result