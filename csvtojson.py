import csv
import json
def csv_to_json(csvFilePath, jsonFilePath):
    #initialize your json file
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        #read csv as dictionary data
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            #outer key of nested dictionary
            key = rows[someKey]
            #only select rows which matches the condition
            if rows[criteriaKey]==condition:
                data[key]=rows
                
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        #write to json
           jsonf.write(json.dumps(data, indent=4)) 
csvFilePath = r'xyz.csv'
jsonFilePath = r'abc.json'
csv_to_json(csvFilePath, jsonFilePath)
