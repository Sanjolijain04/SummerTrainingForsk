# regular expressions
import re
#input 
card_number=input("Enter your card number: ")
patt=re.match(r'[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})',card_number)

conse=re.search(r'(\d)\1{3,}',card_number.replace('-',''))

if patt and not conse:
    print("Valid")
else:
    print("Invalid")