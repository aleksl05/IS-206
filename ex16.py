from sys import argv

script, filename = argv

print "First we are going to print everything"
print "in that file, so that we know what we are deleting"
file = open(filename, 'r')
print file.read()

raw_input("When you are finish reading the file, press return")

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and now we are going to print whats in the new file"

print file.read()

raw_input("press enter when finished")

print "And finally, we close it."
target.close()