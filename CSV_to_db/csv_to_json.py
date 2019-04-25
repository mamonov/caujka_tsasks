import csv
import json
import datetime

csvfilepath = "statistic_data.csv"
jsonfilepath = 'amenities.json'

data = []
x = 0
with open(csvfilepath) as csvfile:
    csvreader = csv.reader(csvfile)
    for csvrow in csvreader:
        data.append(
            "INSERT INTO `counters`(`date`, `gas`, `water`, `electricity_day`, `electricity_night`, `electricity_overall`) VALUES(" + "'" +
            datetime.datetime.strptime(csvrow[0], "%d.%m.%Y").strftime("%Y-%m-%d") + "', " + "'" + csvrow[
                1] + "', " + "'" + csvrow[2] + "', " + "'" + csvrow[3] + "', " + "'" + csvrow[
                4] + "', " + "'" + csvrow[5] + "');")

with open(jsonfilepath, "w") as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))
