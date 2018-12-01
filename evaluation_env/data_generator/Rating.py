class Rating:
	def __init__(self, customer, coffee, rating):
		self.customer = customer
		self.coffee = coffee
		self.rating = rating

	def getCustomer(self):
		return self.customer

	def getCoffee(self):
		return self.coffee

	def getJson(self):
		output = {
			'customer' : self.customer.getName(),
			'coffee' : self.coffee.getName(),
			'rating' : self.rating
		}
		return output
