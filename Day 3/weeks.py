#missing week values
#input tuple
weeklist=tuple((input("Enter your list of days: ").split()))

#tuple to list
weeklist=list(weeklist)

#days list
days_list=['monday','tuesday','wednesday','thursday','saturday','sunday']

#insert missing days
for item in days_list:
    if item not in weeklist:
        weeklist.append(item)

#list to tuple
print(tuple(weeklist))