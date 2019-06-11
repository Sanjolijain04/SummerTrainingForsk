#last line of a file
name=input("Enter the file name : ")
with open(name, mode='w') as fp:
    print("Enter the content of file: ")
    while(True):
        new=input(">")
        if not new:
            break
        else:
            fp.write(new+"\n")
    

with open(name, mode='rt') as fp:
    print("Final line of file: ")
    lineList=fp.readlines()
    print(lineList[-1])