# anagrams

str1=input("Enter the string one: ")
str2=input("Enter the string two: ")
list1=[]
#check each alphabet
for item in str1:
    if item in str2:
        list1.append(True)
    else:
        list1.append(False)
#check anagram
if False in list1:
    print ("Not anagram")
else:
    print ("Anagram")