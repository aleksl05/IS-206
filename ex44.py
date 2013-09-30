class Parent(object):

	def implicit(self):
		print "Parent implicit()"
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

class Parent2(object):
	def override(self):
		print "PARENT override()"
		
class Child2(Parent):
	def override(self):
		print "CHILD override()"
		
dad = Parent2()
son = Child2()

dad.override()
son.override()