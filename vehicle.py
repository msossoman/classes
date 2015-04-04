class Vehicle(object):

	def __init__(self, name, wheels, color):
		self.name = name
		self.wheels = wheels
		self.color = color

	def getName(self):
		return self.name

	def numberWheels(self):
		print int(self.wheels)
		if self.wheels > 4:
			print "You're vehicle is a truck."
		else:
			print "You're vehicle is a car."

	def getColor(self):
		return self.color
	

