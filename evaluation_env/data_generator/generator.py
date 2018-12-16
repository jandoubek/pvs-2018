'''
Skript pro generování uživatelských recenzií pro jistou množinu kávy.
Kávy jsou zeskupené do skupin (kaváren) a každá skupina (kavárna) má svoji základní kvalitu.
Kavlita kávy se pak může mírně lišit od této základní kvality kavárny,
ale pořád by kavárna měla dosahovat v průměru dané kvality.
Výsledné uživatelské hodnocení je ještě ovlyvněno také (ne)odborností hodnotitelů,
které zašumuje výsledné recenze.

Ve výsledku by však měl hodnotitel hodnotit kávy ze stejné kávarny přibližně stejně.

Výsledek skriptu je soubor example_data.json, který obsahuje uživatelské recenze ve formátu JSON.
Každý uživatel hodnotí káždou kávu právě jednou,
tj. celkový počet recenzí je roven součinu počtu uživatelů a počtu káv
'''
import json, random
from evaluation_env.data_generator.Cafe import *
from evaluation_env.data_generator.Coffee import *
from evaluation_env.data_generator.Customer import *
from evaluation_env.data_generator.Rating import *
import math

# Definice počtů jednotlivých objektů
cafeCount = 5
coffeeCount = 50
customerCount = 15

# Hodnota základní kvality kavárny ma rovnoměrné rozdělení od 0 po 100
# Ve finálním hodnocení kávy je pak ještě zohledněn druh kávy a zkušenosti uživatele
# Velikosti rozptylů káv a uživatelů, které ovlyvňují výslední hodnocení kávy
cafeMinQuality = 10
cafeMaxQuality = 90
coffeeVariance = 16
customerVariance = 8
criteria = ['coffeeTaste', 'cafeAtmosphere', 'baristaSkills', 'cafeCosiness', 'cafeStyle']

cafeList = []
coffeeList = []
customerList = []
ratingList = []
ratingCount = customerCount * coffeeCount

# Inicializace generátoru náhodných čísel
random.seed(42)

# Inicializace kaváren s rovnoměrným rozdělením kvality
for i in range(cafeCount):
	cafeQuality = random.randint(cafeMinQuality, cafeMaxQuality)
	cafe = Cafe('cafe_' + str(i), cafeQuality)
	cafeList.append(cafe)

# Inicializace kávy s gaussovským rozdělením kvality
# Střední hodnota kvality kávy je rovna základní kvalitě kavárny
# Kávy jsou rovnoměrně přidělované ke kavárnam, v součtu je tak dosažen požadovaný počet káv
for i in range(coffeeCount):
	cafe = cafeList[i % cafeCount]
	coffeeQuality = round(random.gauss(cafe.getQuality(), coffeeVariance))
	coffee = Coffee('coffee_' + str(i), cafe, coffeeQuality)
	coffeeList.append(coffee)

# Inicializace uživatelů - zatím přepokladáme uživatelé bez zkušeností (rozptyl je stejný pro všechny)
# Postupně by však uživatele mohli nabývat zkušenosti a jejich rozptyl hodnocení se muže zmenšovat
for i in range(customerCount):
	customer = Customer('customer_' + str(i))
	customerList.append(customer)

# Generování uživatelských recenzí - každý uživatel hodnotí každou kávu
# Výsledné hodnocení má gaussovské rozdělení se střední hodnotou rovnou kvalitě kávy a definovaným rozptylem
for customer in customerList:
	for coffee in coffeeList:
		ratingValues = {}
		for criterion in criteria:
			criterionValue = round(random.gauss(coffee.getQuality(), customerVariance))
			ratingValues[criterion] = max(min(criterionValue, 100), 1)
		ratingValues['coffeeTaste'] = math.ceil(ratingValues['coffeeTaste'] / 20)
		ratingValues['cafeAtmosphere'] = math.ceil(ratingValues['cafeAtmosphere'] / 20)
		ratingValues['baristaSkills'] = math.ceil(ratingValues['baristaSkills'] / 20)
		ratingValues['cafeCosiness'] = math.ceil(ratingValues['cafeCosiness'] / 50) - 1
		ratingValues['cafeStyle'] = math.ceil(ratingValues['cafeStyle'] / 50) - 1
		rating = Rating(customer, coffee, ratingValues)
		ratingList.append(rating)

output = []
for rating in ratingList:
	output.append(rating.getJson())

random.shuffle(output)
file = open('example_data.json', 'w')
json.dump(output, file, indent = 4)
print('Celkem bylo vygenerováno ' + str(len(ratingList)) + ' recenzií')
