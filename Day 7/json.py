import requests
import json


url1 = "http://api.openweathermap.org/data/2.5/weather"
query_url="?q="+input("Enter city name: ")
api_key="&appid=8b3a91120f287c33eff8e8fa793dd236"

url=url1+query_url+api_key

response=requests.get(url)
jsondata=response.json()

for key, value in jsondata.items():
    print(key, ":", value, "\n")




