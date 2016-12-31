class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "Price: ${}.".format(self.price)
		print "Maximum speed: {} miles per hour.".format(self.max_speed)
		print "Total mileage: {} miles".format(self.miles)
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		if self.miles - 5 < 0:
			print "Cannot reverse any further"
			self.miles = 0
		else:
			self.miles -= 5
		return self

b1 = Bike(150, 45)
b2 = Bike(250, 55)
b3 = Bike(350, 65)

b1.ride().ride().ride().reverse().displayInfo()
b2.ride().ride().reverse().reverse().displayInfo()
b3.reverse().reverse().displayInfo()