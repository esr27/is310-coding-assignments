#I will be using a python wrapper for Wikipedia's API to gather data.
#To install this package, run the following command in your terminal: pip install wikipedia-api
#No api key necessary! (Still need a key for pyeuropeana though)

import wikipediaapi
import pandas as pd
import pyeuropeana.apis as apis
import os
import apikey

EUROPEANA_API_KEY = apikey.load("europeana")
os.environ["europeana"] = EUROPEANA_API_KEY

wiki_wiki = wikipediaapi.Wikipedia('IS310 API test (esr@illinois.edu)', 'en')

na_capitals = [
    "St._John's,_Antigua_and_Barbuda",
    "Nassau,_Bahamas",
    "Bridgetown",
    "Belmopan",
    "Ottawa",
    "San_José,_Costa_Rica",
    "Havana",
    "Roseau",
    "Santo_Domingo",
    "San_Salvador",
    "St._George's,_Grenada",
    "Guatemala_City",
    "Port-au-Prince",
    "Tegucigalpa",
    "Kingston,_Jamaica",
    "Mexico_City",
    "Managua",
    "Panama_City",
    "Basseterre",
    "Castries",
    "Kingstown",
    "Port_of_Spain",
    "Washington,_D.C."
]


data = []

for city in na_capitals:
    response = apis.search(query=city)
    image_link = next((item.get('edmIsShownBy') for item in response['items'] if item.get('edmIsShownBy')), None)[0]
    page_py = wiki_wiki.page(city)
    summary = page_py.summary[0:100]
    data.append({
        'Capital City': page_py.title,
        'Summary': summary,
        'Media Link': image_link
    })
    print(page_py.title + ":\n" + summary)
    print(image_link)
    print("\n")

df = pd.DataFrame(data)
df.to_csv('na_culture_data.csv', index=False)