# supermarket 

from collections import OrderedDict
od=OrderedDict()

#dictionary


#input dictionary
while(True):
    new_item=(input("Enter the items with their prices: ")).split()
    if not new_item:
        break
    else:
        k=" ".join(new_item[:-1])
        if k in od:
            od[k]+=int(new_item[-1])
        else:
            od[k]=int(new_item[-1])
        
        
        
    
    
    
print(od)