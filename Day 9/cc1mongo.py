from pymongo import MongoClient

client=MongoClient("mongodb://sanjolijain04:sanjoli%401166@cluster0-shard-00-00-cdpt6.mongodb.net:27017,cluster0-shard-00-01-cdpt6.mongodb.net:27017,cluster0-shard-00-02-cdpt6.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb=client.my_database

def add_student(name, age, roll_no, branch):
    unique_student=mydb.my_collection.find_one({"Student_Name" : name })
    if unique_student:
        return "Students already exists."
    else:
        mydb.my_collection.insert_many(
                {
                    "Student_Name" : name,
                    "Student_Age" : age,
                    "Student_Roll_no" : roll_no,
                    "Student_Branch" : branch
                    
                } )
        return "Student Added Succesfully"
    
def fetch_all_student():
    user=mydb.my_collection.find()
    for item in user:
        print(item)
        
add_student('Sanjoli',20,29,'CSE')
add_student('Ankit',18,49,'ECE')
add_student('Rocky',20,18,'CSE')
add_student('Saman',14,54,'IT')
add_student('Pragya',19,51,'ECE')
add_student('Nidhi',20,16,'ME')
add_student('Ram',17,11,'CSE')
add_student('Payal',10,45,'EE')
add_student('Anuu',18,27,'EE')
add_student('Sagar',18, 23,'CV')

fetch_all_student()


