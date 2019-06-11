# centered average

my_array=list(map(int,(input("Enter the array: ")).split()))
my_array2=[]

for item in my_array:
    my_array2.append(item)

my_array2.sort()
my_array2=my_array2[1:len(my_array2)-1]

#sum of array elements
sum=0
for item in my_array2:
    sum=sum+item
    #calculate average
centered_average=sum/len(my_array2)
print("CEntered average is: ", centered_average)
    