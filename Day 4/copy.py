# copy file

#open source file
fp=open("romeo.txt","rt")

#open destination file
fp1=open("romeo3.txt","w")

#copy to destination file
for line in fp:
    fp1.write(line)
fp.close()
fp1.close()

#print content of destination file
fp1=open("romeo3.txt","rt")
print(fp1.read())
fp1.close()