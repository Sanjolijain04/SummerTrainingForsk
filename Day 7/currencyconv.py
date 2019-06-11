import requests
import json


url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=4553c6e5393b2e40b6c6"
response = requests.get(url)
jsondata=response.json()
print(jsondata)
amount=int(input("Enter the amount: "))
print("Converted: ",jsondata['USD_INR'] * amount)









