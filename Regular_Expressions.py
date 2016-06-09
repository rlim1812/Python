'''
Ryan Lim
Using Python to Access Web Data
Concept: Regular Expressions
Program Purpose:
Use regular expressions in Python
to parse through a text file and
sum up all the integers that are found
'''

#module
import re

#initializations
list_of_values = []
total = 0

#create a file object to get access to a text file
file_object = open("Actual_Data.txt")

#iterate through the file and find all of the integers
for line in file_object:
    line = line.rstrip()
    list_of_integers = re.findall("[0-9]+", line)
    list_of_values = list_of_values + list_of_integers

#convert each value in list to an integer and add it to the running total
for number in list_of_values:
    number = int(number)
    total = total + number

print(total)