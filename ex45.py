from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		print "Comming soon"
		exit(1)
		
class Engine(object):
	def __init__(self,scene_map):
		self.scene_map = scene_map
		self.notebook = Notebook()
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n----------------------"
			next_scene_name = current_scene.enter()
			
class Hall(Scene):

	def enter(self):
		self.notebook = Notebook()
		print "You have entered a house, the mission is to check"
		print "every room and collect letters to guess a word."
		print "You can store letters in your notebook with 'save letters'"
		
		
		
		action = raw_input("> ")
		
		if action == "check notebook":
			notebook.checkBook()
		else:
			return 'Hall'
			
class Livingroom(Scene):
	
	def enter(self):
		print "Kommer vel noe fornuftig snart"
		
class Bathroom(Scene):

	def enter(self):
		print "Beskrivelse av badet kommer snart"
		
class Bedroom(Scene):

	def enter(self):
		print "Soverommet"
		
class Kitchen(Scene):
	
	def enter(self):
		print "Kjoekenet"
		
class Notebook(object):

	def	__init__(self):
		self.notebook = []

	def checkBook(self):
		if len(notebook) == 0:
			print "There is nothing in the notebook"
		else:
			print notebook
		
		
class Map(object):

	scenes = {
		'Hall': Hall(),
		'Kitchen': Kitchen(),
		'Livingroom': Livingroom(),
		'Bedroom': Bedroom(),
		'Bathroom': Bathroom()
		}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
			
a_map = Map('Hall')
a_game = Engine(a_map)
a_game.play()
		
		
		
	
