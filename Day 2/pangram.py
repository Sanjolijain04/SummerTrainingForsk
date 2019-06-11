# pangram
import string
my_string=input("Enter a string: ").lower()
a_z=list(string.ascii_lowercase)
a_z.insert(0," ")
my_string2=[]

for item in my_string:
    if item not in my_string2:
        my_string2.append(item)

        

my_string2.sort()

if(a_z==my_string2):
    print("Pangram")
else:
    print("Not Pangram")