
from asyncio.windows_events import NULL
from platform import win32_edition
from tkinter.messagebox import RETRY

from jinja2 import UndefinedError; win32_edition
import os
import math 
 
#---Task 1---
# Returns True if the input string has more vowels than consonants
# Returns False if the input string has more consonants than vowels
# Returns None (this is the Python equivalent of null) if the input string has an equal number of consonants and vowels. We’ll ignore type safety for now!

def more_vowels_than_constants(str):
    vowel_count = 0
    const_count = 0
    for i in str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowel_count += 1
        else:
            const_count += 1
    if vowel_count > const_count:
        return True
    elif vowel_count < const_count:
        return False
    else:
        return NULL
print(more_vowels_than_constants("Python"))
   
# ---Task 2---
# The volume of a cylinder is given by the formula V = πhr^2. Given a radius R and height H as inputs return the volume of a cylinder with radius R and height H
def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume
print(cylinder_volume(3,5))

#---Task 3---
# Comma-separated values (CSV) is a popular format for storing data. For the first step of the CSV portion of this assignment, write a function that takes a list of strings as inputs, and returns a single string created by joining all the input strings together, with a comma separating them.
def csv_strings(names):
    names = ['Sade', 'John', 'Ahmed']
    ','.join(names)
    return names
print(csv_strings(['Josh', 'Chris', 'Jacob']))
#---Task 4---
# Now write another function that takes a list of lists of strings, 
# applies the operation from question 3 to each list, and writes the result as a row 
# of an output file. The function should return the path to the file where the strings were written.
def abspath(list_strings):
    list_strings = [['s', 'i', 'd', 'r'],['e', 'f'],['g', 'h', 'i']]
#using join function to combine lists
#create file and path and returning path where strings were written
    ' '.join(list_strings)
    file = open('list_strings', 'a')
    file.write("I am writing to a file")
    file.close()
    return file

#---Task 5---
# Finally, write the reverse of question 4: write a function that takes in a filename (which we will assume is a CSV), and 
# returns a list of lists of strings, where one row in the file corresponds to one 
# list in the output list (and each value between the commas in the file row is one element in the list).
def reverse(csv):
    csv = [['s', 'i', 'd', 'r'],['e', 'f'],['g', 'h', 'i']]
    ','.join(csv)
    file = open('csv', 'r')
    print(file.read())
    return csv

#---Task 6---
# Error-handling is an important part of writing web apps, 
# especially when your app talks to potentially unreliable third-party APIs. 
# This problem will have you practice the try/except keywords in Python. 
# Write a function that takes two numbers and divides the first one by the second. 
# You should catch the error if the second number is zero and print a warning instead of crashing.
try:
    def two_nums(a,b):
        divisor = a/b
        return divisor
except ZeroDivisionError:
    print("warning")

#---Task 7---
# Write a function that takes a list of integers and returns the same list, but without any duplicates.
def no_duplicates(int_list):
    int_list = {1,2,3,4}
    return int_list
print (no_duplicates({1,2,3,4}))

#---Task 8---
# In Python, you can write code that interacts with other parts of your operating system. 
# Write a function that creates a new folder called “hw3-folder” inside the current directory (the one where your code is running).

def new_folder():
    hw3 = os.getcwd()
    final_directory = os.path.join(hw3, r('hw3-folder'))
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)



