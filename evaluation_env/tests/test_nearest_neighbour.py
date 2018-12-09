import unittest
import json

from nearest_neighbour import NearestNeighbour

class GeneralTest(unittest.TestCase):

	def test_first(self):
		customerRating = {
			"customer": "customer_7",
			"coffee": "coffee_21",
			"rating": {
				"aroma": 41,
				"environment": 33,
				"color": 37,
				"taste": 54,
				"smell": 28,
				"service": 54
			}
		}
		with open('../data_generator/example_data.json') as file:
			data = json.load(file)
			nn = NearestNeighbour(data)
			suggestedCoffee, nearestCustomer = nn.getSuggestion(customerRating)
			print("Doporučené kafe je " + suggestedCoffee + " hodnocené uživatelem " + nearestCustomer)
			self.assertTrue(suggestedCoffee == "coffee_15" and nearestCustomer == "customer_9")