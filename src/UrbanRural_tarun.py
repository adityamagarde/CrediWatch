import pgeocode
import re
import json
import pandas as pd

def findCityTier(adress):
    with open('../data/cities.json') as f:
      json_data = json.load(f)
    
    tier1 = []
    tier2= []
    for index in range(0,50):
        tier1.append(json_data[index]['name'].lower())
        
    for index in range(50,100):
        tier2.append(json_data[index]['name'].lower())
    
    
    
    nomi = pgeocode.Nominatim('in')
    zip_pattern = '(\d{6})'  
    #print(re.search(zip_pattern,adress))
    zip_code = re.search(zip_pattern,adress).group(1)
    city_detail = nomi.query_postal_code(zip_code)                      #Taking adress details from pincodde
    city_name = str(city_detail.county_name).lower()
    #print(city_name)
    for city in tier1:
        if((city in city_name) or (city_name in city)):
            return 1
        
    for city in tier2:
        if((city in city_name) or (city_name in city)):
            return 2
        
    return 3

if __name__ == '__main__':
    findCityTier('C/o Mindarika Private LTD Dekawada DETROJ Ahmedabad-382120 Gujarat')

