i = 0
numbers = []
numbers2 = []

def loop(end, first):
	i = 0
	while i < end:
		print "At the top i is %d " %i
		numbers.append(i)
		
		i = i + first
		print "Numbers now: " , numbers
		print "At the bottom i is %d " %i
		
def second_loop(end, first):
	i= 0
	for i in range(end, first):
		print "Her paa toppen saa er i: %d" % i
		numbers2.append(i)
		
		i = i + first
		print "Numrene naa " , numbers
		print "Paa bunnen er i: %d" %i

number = raw_input("Give me a number ")
number = int(number)
second_number = raw_input("Give me a second number ")
second_number = int(second_number)


loop(number, second_number)
second_loop(5, 1)
		
	
	
print "The numbers: "

for num in numbers:
	print num
	
print "The numbers from the second list"

for numz in numbers2:
	print numz
	
	
