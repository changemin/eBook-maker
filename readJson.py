import json

with open('config.json') as json_file:
    data = json.load(json_file)
    
    PoemNum = str(data['DATASET']['PoemNum'])
    BGNum =  str(data['DATASET']['BGNum'])

print("PoemNum : " + PoemNum)
print("BGNum : " + BGNum)