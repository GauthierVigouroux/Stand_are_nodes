import json

#Lecture initial du fichier json
def readJsonFile():
    # Doit retourner le dico sous sa bonne forme
    fileObject = open("isolist.json", "r")
    jsonContent = fileObject.read()
    InitISODict = json.loads(jsonContent)
    ISODict = dict()
    for cle,values in InitISODict:
        ISODict["cle"]=[values[0],values[1],tuple()]
    return ISODict