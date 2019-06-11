# regular expressions

#import library for regular expression
import re

#check that input is floating number
number=input("Enter a floating point number: ")
#use of regular expression
if re.fullmatch(r'\+?\-?\.?[0-9]*\.[0-9]*',number):
    print("True")
else:
    print("False")
