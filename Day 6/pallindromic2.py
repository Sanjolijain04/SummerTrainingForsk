# pallindromic integer 2

input_list=(input("Enter the list of numbers: ").split())
print(all(int(item)>0 for item in input_list) and any(item[::-1]==item for item in input_list))




