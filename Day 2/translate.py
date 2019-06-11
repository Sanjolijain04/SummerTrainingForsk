# translate the string

def translate_string(my_string):
    consonants='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for item in my_string:
        if item in consonants:
            translates_string.append(item+'o'+item)
        else:
            translates_string.append(item)
            
    return "".join(translates_string)
            
    

my_string=input("Enter the string: ")
translates_string=[]
print(translate_string(my_string))