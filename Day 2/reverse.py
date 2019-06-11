#reverse string

def reverse(my_string):
    rev_string=my_string[::-1]
    return rev_string
my_string=input("Enter String: ")

print(reverse(my_string))