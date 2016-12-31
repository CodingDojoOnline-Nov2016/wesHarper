class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
	def display_all(self):
		print "Price: ${0}, Speed: {1}mph, Fuel: {2}, Mileage: {3}mpg, Tax: {4}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
		return self

c1 = Car(2000, 35, "Full", 15)
c2 = Car(2000, 5, "Not Full", 105)
c3 = Car(2000, 15, "Kind of Full", 95)
c4 = Car(2000, 25, "Full", 25)
c5 = Car(2000, 45, "Empty", 25)
c6 = Car(20000000, 35, "Empty", 15)

c1.display_all()
c2.display_all()
c3.display_all()
c4.display_all()
c5.display_all()
c6.display_all()