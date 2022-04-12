import jsonreading
import PARSE_HTML.parse_html
import json

#Récupération du dico original
ISODict = dict()
ISODict = jsonreading.readJsonFileInit("isolist.json")
compteur = 0
#Récupération des infos sur le site de l'ISO afin de compléter les tuples des différents liens
for standard in list(ISODict.items()):
    #print(standard[1][1])
    ISODict = PARSE_HTML.parse_html.isorequests(standard[1][1],ISODict)
    compteur = compteur + 1
    print(compteur)
    print(standard[0])
    #print(list(ISODict.items())[-1]) #Permet de voir l'évolution de la taille du dico
with open('data.json', 'w') as fp:
    json.dump(ISODict, fp, sort_keys=True, indent=4)