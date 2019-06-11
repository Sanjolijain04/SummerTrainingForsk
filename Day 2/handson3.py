# hands on 3
import handson2

def days_in_month(month):
    if(month==2):
        return 29
    elif(month%2==0):
        return 30
    else:
        return 31
    
month=int(input("Enter the month :"))
print(days_in_month(month))