# Fizzbuzz
number=1
while(number<=100):
    if(number%3==0 and number%5==0):    #divided by both
        print("fizzbuzz")
        number=number+1
    elif(number%5==0):                  #divided by 5
        print("buzz")
        number=number+1
    elif(number%3==0):                     #divided by 3
        print("fizz")
        number=number+1
    else:                                 #divided niether by 3 nor by 5
        print(number)
        number=number+1