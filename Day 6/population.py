#population count
import csv

from collections import defaultdict

with open("population.csv") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    csv_list=list(csv_reader)


pop_dict=defaultdict(int)
for item in csv_list:
    k="India "+item[-1]
    pop_dict[k]+=int(item[-2].replace(",",""))
        
print(pop_dict)



    
    



  
    




    

