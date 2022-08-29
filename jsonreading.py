import json

#Initial reading of the json file
def readJsonFileInit(file):
    # Must return the dictionary in its correct form
    # fileObject = open(file, "r")
    # jsonContent = fileObject.read()
    with open(file, 'r') as fp:
        InitISODict = json.load(fp)
    ISODict = dict()
    for cle,values in InitISODict.items():
        ISODict[cle]={
            "nom":values["nom"],
            "short":values["short"],
            "dependance":[],
            "global_count_citation": 0
        }
    return ISODict

def readJsonFileViz(file):
    fileObject = open(file, "r")
    jsonContent = fileObject.read()
    Dicoviz=json.loads(jsonContent)
    return Dicoviz