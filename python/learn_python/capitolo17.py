"""
Bagnis Gabriele
LEARN PYTHON 3 THE HARD WAY capitolo 17
"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()

#I must use the out_file.close () command to free the memory area occupied by him. 
#This is more useful when the script continues because it frees memory and blocks accidental changes to the file.