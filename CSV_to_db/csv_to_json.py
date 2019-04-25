import csv
import json

csvfilepath = "statistic_data.csv"
jsonfilepath = 'amenities.json'

data = {}
x = 0
with open(csvfilepath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for csvrow in csvreader:
        print(csvrow)
        data[x] = csvrow
        x += 1

with open(jsonfilepath, "w") as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))
