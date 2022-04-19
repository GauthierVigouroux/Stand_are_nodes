import jsonreading
import PARSE_HTML.parse_html
import json

#Récupération du dico original
ISODict = dict()
ISODict = jsonreading.readJsonFileInit("isolist.json")
ISODictAntiCircular = ISODict
#Récupération des infos sur le site de l'ISO afin de compléter les tuples des différents liens
#.items() retourne un tuple donc hashable
for standard in ISODictAntiCircular:
    print(standard)
    ISODict[standard] = PARSE_HTML.parse_html.isorequests(ISODict[standard]["lien"],ISODict)
    #print(list(ISODict.items())[-1]) #Permet de voir l'évolution de la taille du dico
    print(ISODict[standard])
print(ISODict)
with open('data.json', 'w') as fp:
    json.dump(ISODict, fp, sort_keys=True, indent=4)