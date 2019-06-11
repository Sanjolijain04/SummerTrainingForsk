#weighted score calculator

print("Maximum marks are 100 for both assignments and exams ")
assign1=int(input("Enter the marks of assignment 1: "))
assign2=int(input("Enter the marks of assignment 2: "))
assign3=int(input("Enter the marks of assignment 3: "))
exam1=int(input("Enter the marks of exam 1: "))
exam2=int(input("Enter the marks of exam 2: "))

#calculate weighted score
weighted_score=(assign1+assign2+assign3)*0.1 + (exam1+exam2)*0.35

print("Weighted score: ", weighted_score)