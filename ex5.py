my_name = 'Aleksander Lund'
my_age = 27 #Dette er korrekt
my_height = 181 #cm
my_weight = 75 #kg
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'brown'

print "Let`s talk about %s. "% my_name
print "He's %d cm tall. " %my_height
print "That is %f inches tall " %(my_height / 2.54)
print "He's %d kg heavy. " %my_weight
print "That is %f pound. " % (my_weight *  2.20462262185 )
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair. " % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee. " %my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)