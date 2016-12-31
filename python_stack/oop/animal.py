class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display_health(self):
		print "{0} has {1} health.".format(self.name, self.health)
		return self

animal = Animal("animal")
animal.walk().walk().walk().run().run().display_health()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

karl = Dog("Karl")
karl.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		print "this is a dragon!"
		super(Dragon, self).display_health()

ralphie = Dragon("Ralphie")
ralphie.walk().walk().walk().run().run().fly().fly().display_health()

#Check to see if parent class does not reverse inherit from children. Should throw errors.

# animal.fly()
# animal.pet()