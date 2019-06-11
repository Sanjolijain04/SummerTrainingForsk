# Pattern 

number=int(input("Enter the number: "))
for i in range(1,number+1):
    print("* "*i)
    if(i==number):
        while(i>=1):
            print("* "*(i-1))
            i-=1