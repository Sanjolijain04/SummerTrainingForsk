# sorting

student_list=[]

while(True):
    
    user_input=input("Enter the name,age,score of student: ")\
    
    if not user_input:
        break
    
    name,age,marks=user_input.split(",")
    
    student_list.append((name, int(age), int(marks)))
    
    
student_list.sort()
print(student_list)