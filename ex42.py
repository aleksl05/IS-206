## Animal is-a object, look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal-object
class Dog(Animal):

	def __init__(self, name):
		#Here we define the name to the Dog(Animal)
		self.name = name
		
## Cat is-a Animal-object
class Cat(Animal):

	def __init__(self, name):
		## Defining the name to the Cat
		self.name = name
		
##Person is-a object
class Person(object):

	def __init__(self, name):
		##This is one of persons attributes, name.
		self.name = name
		
		##Person has-a pet of some kind
		self.pet = None
		
##Employee is-a person object.
Class Employer(Person):

	def __init__(self, name, salary):
		## Hmm, what is this strange magic?
		super(Employee, self).__init__(name)
		## Defining the salary attribute.
		self.salary = salary
		
##Fish is-a object
class Fish(object):
	pass
	
##Salmon is-a object of fish
class Salmon(Fish):
	pass
	
##Halibut is-a fish-object
class Halibut(Fish):
	pass
	
	## rover is-a Dog
rover = Dog("Rover")

##satan is-a Cat object
satan = Cat("Satan")

##mary is-a person-object
mary = Person("Mary")

##mary has-a pet which is satan the cat-object.
mary.pet = satan

##employee has-a frank which is a person object, but employee is also a person-object
frank = Employee("Frank", 120000)

## frank has-a pet which is rover which is a dog-object that is a animal-object
frank.pet = rover

##Flipper is-a fish object
flipper = Fish()

##crouse is-a salmon-object which is a fish-object
crouse = Salmon()

##harry is-a halibut-object which is a fish-object
harry = Halibut()