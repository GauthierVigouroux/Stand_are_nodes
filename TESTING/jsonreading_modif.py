import json

#Lecture initial du fichier json
def readJsonFileInit(file):
    # Doit retourner le dico sous sa bonne forme
    # fileObject = open(file, "r")
    # jsonContent = fileObject.read()
    with open(file, 'r') as fp:
        InitISODict = json.load(fp)
    ISODict = dict()
    for cle,values in InitISODict.items():
        ISODict[cle]={
            "nom":values["nom"],
            "lien":values["lien"]
        }
    return ISODict

def readJsonFileViz(file):
    fileObject = open(file, "r")
    jsonContent = fileObject.read()
    Dicoviz=json.loads(jsonContent)
    #TODO voir pour une réorganisation du dico
    return Dicoviz