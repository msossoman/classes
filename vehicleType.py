# The subclasses Truck and Car are not working properly, and I can't figure out how to fix them.

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

class Truck(Vehicle):

	def __init__(self, name, fuel):
		Vehicle.__init__(self)
		self.fuel = fuel

	def fuelType(self):
		return self.fuel

	def __str__(self):
		return "Your truck takes %s as it's fuel." % (self.fuel)

class Car(Vehicle):

	def __init__(self, name, doors):
		Vehicle.__init__(self)
		self.doors = doors

	def numberDoors(self):
		if self.doors == 4:
			print "You drive a sedan."
		elif self.doors == 2:
			print "You drive a coupe."
		elif self.doors == 0:
			print "Either you drive a motorcyle, or a bicyle, or it's time for a new car!"