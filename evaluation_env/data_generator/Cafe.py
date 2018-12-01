class Cafe:
	def __init__(self, name, quality):
		self.name = name
		self.quality = max(min(quality, 100), 0)

	def getName(self):
		return self.name

	def getQuality(self):
		return self.quality