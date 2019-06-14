import requests
import cv2
import os

#get api key 
API_KEY="0f84ebbc47644f9d87f930f2c65e9bb5"

#give path
path=(r"C:\Users\admin\Desktop\SummerTrainingForsk\Day 29\Pokemons")

#maximun number of images that can be be folder
max_results=250

#number of photos to be download of an entry
group_size=50

#if folder not present make folder
if not os.path.isdir(path):
    os.mkdir(path)
    
#give url of bing search
url="https://api.cognitive.microsoft.com/bing/v7.0/images/search"

#make a list of names of pokemons to be download
pokemons=[]


#take name of pokemon from user and append in list of names
while(True):
    name=("Enter Pokemon name: ").lower()
    if not name:
        break
    pokemons.append(name)

for term in pokemons:
    
    #give headers
    #In header we give the subscripion key which provide access to api
    headers={"Ocp-Apim-Subscription-Key": API_KEY}
    #get search parameters
    params={"q" : term, "offset" : 0, "count" : group_size}
    
    #make a search
    print("[INFO] Searching bing api for {}".format(term))
    search=requests.get(url, headers=headers, params=params)
    search.raise_for_status()
    
    #get the results from the search
    results=search.json()
    estNumResults=min(results["totalEstimatedMatches"], max_results)
    print("INFO {} results for {}".format(estNumResults,term))
    
    
    total=0
    folder=path+term
    
    if not os.path.isdir(folder):
        os.mkdir(folder)
        
    
    




