import argparse, json, os

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="migrate config file",action="store_true")
args = parser.parse_args()

if args.m:
    configPath = "../../config.json"
    poemPath = "../poem-txt"
    BGPath = "../background-imgs"

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