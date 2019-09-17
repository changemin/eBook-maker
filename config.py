import json,os

configPath = "config.json"
poemPath = "res/poem-txt"
BGPath = "res/background-imgs"

poemList = os.listdir(poemPath)
BGList = os.listdir(BGPath)

print(poemList)
print(len(poemList))

print(BGList)
print(len(BGList))

data = {"DATASET": {"PoemNum": len(poemList), "BGNum": len(BGList)}}

with open(configPath, "w") as write_file:
    json.dump(data, write_file)

print("-------------DATASET Config-------------")
print("PoemNum : " + str(data['DATASET']['PoemNum']))
print("BGNum : " + str(data['DATASET']['BGNum']))
print("----------------------------------------")

# with open(configPath) as json_file:
#     data = json.load(json_file)





