from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

standard_response = requests.get("https://minecraft.fandom.com/wiki/Mob")


standard_soup = BeautifulSoup(standard_response.text, "html.parser")


#All mobs are in tables with attribute data-description describing the type of mob (eg. Passive mobs, Hostile mobs). the regex picks all that end in "mobs".
elements = standard_soup.find_all('table', attrs={"data-description": re.compile(r".*mobs$")})

mob_names = []
mob_types = []

for table in elements:
    mob_type = table['data-description'].split()[0] #The type of mob is the first word in the table.
    mob_rows = table.find_all('a', title=True) #Mobs are in rows....
    
    for mob in mob_rows:
        mob_names.append(mob['title']) #Name is the title.
        mob_types.append(mob_type)


#Using pandas to easily create df for csv format.
df = pd.DataFrame({
    'Version': 'Standard',
    'Name': mob_names,
    'Type': mob_types
})



df.drop_duplicates(inplace=True)


df.to_csv("mobs.csv", index = False)


