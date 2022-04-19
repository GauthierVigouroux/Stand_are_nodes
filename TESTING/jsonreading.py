import json

#Lecture initial du fichier json
def readJsonFileInit(file):
    # Doit retourner le dico sous sa bonne forme
    fileObject = open(file, "r")
    jsonContent = fileObject.read()
    InitISODict = json.loads(jsonContent)
    ISODict = dict()
    for cle,values in InitISODict.items():
        ISODict[cle]=[values[0],values[1],tuple()]
    return ISODict

def readJsonFileViz(file):
    fileObject = open(file, "r")
    jsonContent = fileObject.read()
    Dicoviz=json.loads(jsonContent)
    #TODO voir pour une réorganisation du dico
    return Dicoviz