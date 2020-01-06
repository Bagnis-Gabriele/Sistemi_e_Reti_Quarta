"""
Bagnis Gabriele
LEARN PYTHON 3 THE HARD WAY capitolo 15
"""

#import the library to read the arguments passed at the beginning of the file execution
from sys import argv

#I extract the two arguments
script, filename = argv

#I open the required file
txt = open(filename)

#I print the name and contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

#I print the name and contents of the file
print("Type the filename again:")
file_again = input("> ")

#I open the required file
txt_again = open(file_again)

#I print the contents of the file
print(txt_again.read())

#I close all the files
txt_again.close()
filename.close()

#for run: py capitolo13.py cap15.txt