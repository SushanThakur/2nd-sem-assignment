class Box:
	def __init__(self, l, b, h):
		self.length = l
		self.breadth = b
		self.height = h
	def getVolume(self):
		return self.length*self.breadth*self.height
	def __str__(self):
		return f'{self.length}x{self.breadth}x{self.height}'

ob1 = Box(5,6,10)
ob2 = Box(5,6,10)

print(ob1)

print(ob1.getVolume())
print(ob2.getVolume())
