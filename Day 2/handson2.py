# hands on 2

year=int(input("Enter the year: "))

#function to check leap year
def check_leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(check_leap(year))