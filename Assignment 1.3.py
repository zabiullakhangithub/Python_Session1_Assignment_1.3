# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:47:53 2018

@author: zabiulla.khan

Assignment 1.3

Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.

"""
#Get the first name from user
first_name = str(input("Enter your first name:"))

#Get the last name from user
last_name = str(input("Enter your last name:"))

# Insert space in between first and last name
full_name = first_name + ' ' + last_name

#print the string in reverse order
print(full_name[::-1])
