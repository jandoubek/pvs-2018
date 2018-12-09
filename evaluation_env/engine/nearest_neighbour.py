import math

# Třída NearestNeighbour vybírá nejlepší dostupné kafé na základě jedné vstupní recenze od "hledajícího" uživatele
# a množiny všech zaznamenaných recenzí

# Vstupy : jedno uživatelské hodnocení od "hledajícího" uživatele, všechna hodnocení od všech uživateľů
# Výstupy: identifikátory doporučovaného kafé a uživatele, který má stejné preference

# Popis algoritmu:
# Algoritmus v prvním krok nalezne jedno uživatelské hodnocení, které je nejblíže zadanému hodnocení "hledajícího" uživatele
# Pak sa vyhledá uživatel, který vytvořil toto nejbližší hodnocení, tj. který hodnotil dané kafe co nejvíce stejně
# U tohto uživatele je předpoklad, že má stejné preference jako původní "hledající" uživatel
# V druhém kroku algoritmus vybere nejlépe hodnocené kafé od uživatele se stejnými preferencemi a toto kafé zvolí jako doporučené pro "hledajícího" uživatele

class NearestNeighbour():

	def __init__(self, records):
		self.records = records

	# Metoda pro výpočet vzdálenosti dvou hodnocení počítána jako Euklidovská vzdálenost dvoch hodnocení
	def getDistance(self, record1, record2):
		rating1 = record1['rating']
		rating2 = record2['rating']
		if len(rating1) != len(rating2):
			return math.inf
		sum = 0
		for criterion in rating1:
			sum += math.pow(rating1[criterion] - rating2[criterion], 2)
		return math.sqrt(sum)

	# Metoda pro výpočet absolutního hodnocení dané kávy, počítána jako Euklidovská vzdálenost od nulového hodnocení
	def getAbsoluteValue(self, record):
		rating = record['rating']
		sum = 0
		for criterion in rating:
			sum += math.pow(rating[criterion], 2)
		return math.sqrt(sum)

	# Metoda pro doporučení vhodného kafe a uživatele, který ho kladně hodnotil
	def getSuggestion(self, customerRecord):

		# Nalezení co nejbližšího hodnocení z množiny všech hodnocení
		nearestRecord = min(self.records, key = lambda record: self.getDistance(customerRecord, record) if record['customer'] != customerRecord['customer'] else +math.inf)

		# Nalezení uživatele, kterému patrři nejbližší hodnocení (má nejspíš stejné preference)
		nearestCustomer = nearestRecord['customer']

		# Nalezení hodnocení s nejlepším skóre patřící uživatelovi se stejnými preferencemi
		bestRatingRecord = max(self.records, key = lambda record: self.getAbsoluteValue(record) if record['customer'] == nearestCustomer else -math.inf)

		# Získání identifikátoru kávy, která byla nejlépe hodnocena uživatelem se stejnými preferencemi
		bestCoffee = bestRatingRecord['coffee']
		return (bestCoffee, nearestCustomer)
