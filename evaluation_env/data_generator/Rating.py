class Rating:
	def __init__(self, customer, coffee, ratingData):
		self.customer = customer
		self.coffee = coffee
		self.ratingData = ratingData

	def getCustomer(self):
		return self.customer

	def getCoffee(self):
		return self.coffee

	def getRatingData(self):
		return self.ratingData.values()

	def getJson(self):
		return {
			'customer' : self.customer.getName(),
			'coffee' : self.coffee.getName(),
			'rating' : self.ratingData
		}
