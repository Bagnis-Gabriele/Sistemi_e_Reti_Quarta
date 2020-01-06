"""
Bagnis Gabriele
LEARN PYTHON 3 THE HARD WAY capitolo 16
"""

#import the library to read the arguments passed at the beginning of the file execution
from sys import argv

#I extract the two arguments
script, filename = argv

#I print the file name and ask the user if he is sure to truncate the file
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

#I open the file in Write mode
print("Opening the file...")
target = open(filename, 'w')

#I empty the file
print("Truncating the file. Goodbye!")
target.truncate()

#I ask the user for three lines
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#I add them to the file
print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 +"\n" + line3 + "\n")

#I reopen the file in Read Mode
print("I'm going to reopen the file in Read Mode")
target.close()
target = open(filename, 'r')

#I print the file
print("I'm going to print the contents of the file.")
print(target.read())

#I close the file
print("And finally, we close the file.")
target.close()

#the opening method used deletes any file with the same name as the one it wants to open. 
#Therefore there is no need for the truncated command.