import csv

#open a csv file
with open("passwd", mode='rt') as user_file:
    #open another csv file in write mode
    with open("passwd_copy.csv", mode='w') as copy_file:
        user_info=csv.reader(user_file, delimiter=':')
        copy_info=csv.writer(copy_file, delimiter=' ')
        for row in user_info:
            copy_info.writerow((row[0],row[2]))
        