class Animal:
	def __init__(self, name, age, color, size):
		self.name=name
		self.age=age
		self.color=color
		self.size=size
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
	def sleep(self, hours, dream):
		print("The Animal ",self.name," is dreaming for ",hours, "of ", dream)


dog = Animal("sadek", 22, "yellow", "tiny")
lion = Animal("nofar", 1, "orange", "big")
dog.print_all()
lion.print_all()
lion.sleep(23,"python")

