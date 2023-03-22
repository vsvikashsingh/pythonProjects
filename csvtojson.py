import csv
import json
def csv_to_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows[someKey]
            if rows[criteriaKey]==condition:
                data[key]=rows
                
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        
           jsonf.write(json.dumps(data, indent=4)) 
csvFilePath = r'xyz.csv'
jsonFilePath = r'abc.json'
csv_to_json(csvFilePath, jsonFilePath)
