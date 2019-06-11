# zoo management

#import csv
import csv


#read csv file 
with open("zoo.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    #print(csv_file.readlines())
    
    
def animals_list():
    dict1={}
    #id_list=[]
    #water_list=[]
    with open("zoo.csv") as csv_file:
        csv_reader=csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for item in csv_reader:
            if item[0] not in dict1:
                #od[item[0]]=(id_list.append(item[1]),water_list.append(item[2]))
                dict1[item[0]] = [[int(item[1])],[int(item[2])]]
            else:
                dict1[item[0]][0].append(int(item[1]))
                dict1[item[0]][1].append(int(item[2]))
    return dict1


def water_needed():
    dict2 = {}
    dict1=animals_list()
    total=0
    for item in dict1:
        #for value in dict1[item][1]:
        dict2[item] = sum(dict1[item][1])
            
    
    return dict2
        
                

def total_water():
    dict1=water_needed()
    total=sum(dict1.values())
    return total
            
print("Animals list: ",animals_list())
print(" ")
print("Water needed: ",water_needed())
print(" ")
print("Total Water needed: ", total_water())

                
        
                
                
                
                
            
            




'''
{"elephant" : [[1001,1002,1003],[500,600,550]], "tiger": []}
'''