'''
Ryan Lim
Python
Programming Practice
Concepts: Classes, Object, Inheritance, and Polymorphism
Program: String Reversal
'''

class string_reverser:

    def reverse (self, string):
        #split the string into multiple strings ands save the strings into a list
        self.list_of_strings = string.split()
        #declare a variable that will hold the reversed string
        self.reversed_string = ""
        #loop through the list of strings backwards and append the strings to a reversed string
        i = len(self.list_of_strings) - 1
        while i >= 0:
            self.reversed_string = self.reversed_string + self.list_of_strings[i] + " "
            i -= 1
        return self.reversed_string

#ask the user for a string and then reverse it
user_string = input("Enter a string and the computer will reverse it: ")
reverser = string_reverser()
new_string = reverser.reverse(user_string)
print("The new string is:", new_string)
