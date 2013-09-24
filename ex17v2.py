from sys import argv
from os.path import exists

script, from_file = argv

in_data = open(from_file).read()
to_file = from_file + "copy"
out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()