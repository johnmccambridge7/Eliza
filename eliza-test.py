#==============================================================
# Dartmouth College, LING28, Winter 2020
# Rolando Coto-Solano (Rolando.A.Coto.Solano@dartmouth.edu)
# Examples for Homework 1: Regular Expressions and
#                          basic Python programming
#==============================================================

# Import libraries for processing of operating
# system input (os,sys), string handling (string) 
# and regular expressions (re)
import os
import string
import sys
import re

# Read the input from the command line
userInput  = input("Enter: ")
# Create the variable output, which will
# contain our response
output = ""

# Create the regular expressions
# You can test your regular expressions in numerous
# websites, such as https://regex101.com/
reHello1 = "I'm (.*)"
reHello2 = "My name is (.*)"
reHello3 = "My name's (.*)"
reHello4 = "I am (.*)"

# print the input
print("You:      " + userInput)

# if the input matches the regular expression:
if (re.compile(reHello1).match(userInput)):
	# Then search for the first capturing group and
	# extract it. Then, use it to construct the string
	# Hello, CAPTUREGROUP1! and put it in the output 
	# variable.
	groupHello = re.search(reHello1,userInput,re.IGNORECASE)
	output = "Hello, " + groupHello.group(1) + "!"
# if the input doesn't match the first regular
# expression, then keep trying to match it to
# the other regular expressions we have.
elif (re.compile(reHello2).match(userInput)):
	groupHello = re.search(reHello2,userInput,re.IGNORECASE)
	output = "Hello, " + groupHello.group(1) + "!"
elif (re.compile(reHello3).match(userInput)):
	groupHello = re.search(reHello3,userInput,re.IGNORECASE)
	output = "Hello, " + groupHello.group(1) + "!"
elif (re.compile(reHello4).match(userInput)):
	groupHello = re.search(reHello4,userInput,re.IGNORECASE)
	output = "Hello, " + groupHello.group(1) + "!"
# if the userInput does not match any of the regular
# expressions, then say that you didn't understand
# what the user wrote.
else:
	output = "I didn't understand you"

# print the output
print("Computer: " + output)