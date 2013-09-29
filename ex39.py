#creates a mapping of state to abbreviation
states = {
	'Vest-Agder': 'VA',
	'Aust-Agder': 'AA',
	'Rogaland': 'RL',
	'Vestfold': 'VF'
}

#creates a basic set of states and some cities in them
cities = {
	'VA': 'Kristiansand',
	'AA': 'Valle',
	'RL': 'Stavanger'
}

#Adding some extra cities
cities['VF'] = 'Sandefjord'

#Printing some cities
print '-' * 10
print "Vest-Agder has: ", cities['VA']
print "Aust-Agder has: ", cities['AA']

#Printing some states
print '-' * 10
print "Vest-Agders abbreviation is: ", states['Vest-Agder']
print "Aust-Agders abbreviation is: ", states['Aust-Agder']

#Do it by using the state then cities dict
print '-' * 10
print "Rogaland has: ",cities[states['Rogaland']]
print "Vestfold has: ",cities[states['Vestfold']]

#Print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s has the city %s" %(state, abbrev)

#print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print " %s has the city %s" % (abbrev, city)

#nov do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print " %s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)
	
if not state:
	print "Sorry, no Texas."
		
#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "the city for the state 'TX' is: %s" % city