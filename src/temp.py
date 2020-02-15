import json

with open(r'../data/dataJson.json', 'r') as myFile:
    listOfCustomers = json.loads(json.load(myFile))


print(listOfCustomers["U85100MH2020NPL335745"])