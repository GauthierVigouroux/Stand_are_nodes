import jsonreading
import PARSE_HTML.parse_html

#Récupération du dico original
ISODict = dict()
ISODict = jsonreading.readJsonFile()

#Récupération des infos sur le site de l'ISO afin de compléter les tuples des différents liens
for standard in list(ISODict.items()):
    #print(standard[1][1])
    ISODict = PARSE_HTML.parse_html.isorequests(standard[1][1],ISODict)
    #print(standard[0])
    #print(list(ISODict.items())[-1]) #Permet de voir l'évolution de la taille du dico