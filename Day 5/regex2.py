# regular expressions
'''
#import library
import re

#taking input
print("Enter the email addresses: ")
email_list=[]
valid_email=[]
#taking list of email
while(True):
    new_email=input(">")
    if not new_email:
        break
    else:
        email_list.append(new_email)
    
for item in email_list:
    if re.fullmatch(r'[a-z0-9]*\-?\_?[a-z0-9]*\@[a-z0-9]*\.[a-z]{2,4}',item):
        valid_email.append(item)
        
print(valid_email)
        
        
    
'''
import re
valid_emails=[]
emails=(input("Enter the emails: ").split())
for item in emails:
    if re.fullmatch(r'[a-z0-9]*\-?\_?[a-z0-9]*\@[a-z0-9]*\.[a-z]{2,4}',item):
        valid_emails.append(item)
print(sorted(valid_emails))
    