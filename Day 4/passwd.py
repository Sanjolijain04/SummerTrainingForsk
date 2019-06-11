# password 

#open file
user_info={}
with open("passwd", mode='rt') as file:
    for line in file:
        if not line.startswith("#"):
            line_content=line.split(":")
            user_info[line_content[0]]=line_content[2]

#sort 
for item in sorted(user_info):
    print("username{}: userid{}".format(item, user_info[item]))
        
        
    
    