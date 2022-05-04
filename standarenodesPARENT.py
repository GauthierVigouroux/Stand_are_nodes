import jsonreading
import PARSE_HTML.parse_html
import json
from GRAPHDATABUILD.global_counting import global_count_citation

#Récupération du dico original
ISODict = jsonreading.readJsonFileInit("isolist_v3.json")
ISODictAntiCircular = list(ISODict)
#Récupération des infos sur le site de l'ISO afin de compléter les tuples des différents liens
#.items() retourne un tuple donc hashable
for standardlink in ISODictAntiCircular:
    print(ISODict[standardlink]["short"])
    ISODict = PARSE_HTML.parse_html.isorequests(standardlink,ISODict)
    #print(list(ISODict.items())[-1]) #Permet de voir l'évolution de la taille du dico
    # print(ISODict[standard])
    ISODict = global_count_citation(ISODict)
#print(ISODict)
with open('data.json', 'w') as fp:
    json.dump(ISODict, fp, sort_keys=True, indent=4, ensure_ascii=False)