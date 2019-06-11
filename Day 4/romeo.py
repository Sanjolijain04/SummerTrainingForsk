# romeo and juliet

#open txt file
with open("romeo.txt", mode='rt') as from_file:
    #read all lines
    lines=from_file.readlines()
    #empty list
    lineList=[]
    #list of list of words
    for item in lines:
        lineList.append(item.split())
    
    #dictionary of words
    word_dict={}
    for value in lineList:
        for item in value:
            if item not in word_dict:
                word_dict[item]=1
            else:
                word_dict[item]+=1

print(word_dict)    
        