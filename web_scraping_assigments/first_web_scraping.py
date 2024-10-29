from bs4 import BeautifulSoup
import requests
import apikey
import pyeuropeana.apis as apis
import os 
#the_one_api_key= apikey.load("THE_ONE_API_KEY")

#authorization_headers = {
#    "Authorization": "Bearer " + the_one_api_key
#}

#url = 'https://the-one-api.dev/v2/character'
#response = requests.get(url, headers=authorization_headers)
#print(response.json())


api_key = apikey.load("europeana")
os.environ["europeana"] = api_key

response = apis.search(query = "Galadriel")

for i in response['items']:
    print(i['guid'])

