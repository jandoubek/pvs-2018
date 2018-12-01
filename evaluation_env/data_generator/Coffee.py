class Coffee:
	def __init__(self, name, cafe, quality):
		self.name = name
		self.cafe = cafe
		self.quality = max(min(quality, 100), 0)

	def getName(self):
		return self.name

	def getCafe(self):
		return self.cafe

	def getQuality(self):
		return self.quality
