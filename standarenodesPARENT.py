import jsonreading
from PARSE_HTML.parsing_accuracy import isorequests
import json

#Récupération du dico original
ISODict = jsonreading.readJsonFileInit("isolist_lite.json")
ISODictAntiCircular = list(ISODict)
#Récupération des infos sur le site de l'ISO afin de compléter les tuples des différents liens
#.items() retourne un tuple donc hashable
for standardlink in ISODictAntiCircular:
    print(ISODict[standardlink]["short"])
    ISODict = isorequests(standardlink,ISODict)
    #print(list(ISODict.items())[-1]) #Permet de voir l'évolution de la taille du dico
    # print(ISODict[standard])
#print(ISODict)
with open('data_lite.json', 'w') as fp:
    json.dump(ISODict, fp, sort_keys=True, indent=4, ensure_ascii=False)