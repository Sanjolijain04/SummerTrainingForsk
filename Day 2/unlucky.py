#unlucky

#taking array input
my_array=list(map(int,(input("Enter array: ")).split()))
my_array2=[]
index_array=[]

#function defination
def unlucky_13(my_array):
    for item in my_array:
        if(item!=13):
            my_array2.append(item)
        else:
            index_array.append(my_array.index(item)+1)

#function call
unlucky_13(my_array)


#removing next item to 13
for item in index_array:
    my_array2.remove(my_array[item])
    break

#print array
print(my_array2)
print(index_array)