import json
import requests

json_data={
"Student" :{
        "Phone Number" : "8560961166",
        "Name" : "Sanjoli Jain",
        "College Name" : "Poornima",
        "Branch" : "CS"
        }
    
}
    
Host="http://13.127.155.43/api_v0.1/sending"
data=json_data
headers={"Content-type" : "application/json", "Content-Length" : len(data), "data" : json.dumps(data)}

def post_method():
    response=requests.post(Host,data,headers)
    return response
print(post_method().text)

def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving")
    return response

print (get_method().text)
    
