# list of absentee

#file in write mode
content=[]
with open('absentee.txt', mode='w') as fp:
    while(True):
        name=input(">")
        
        if not name:
            break
        else:
            fp.write(name+"\n")

        


    
            