from shutil import ExecError
import unicodedata
from requests_html import HTMLSession
import jsonreading

session = HTMLSession()
url = 'https://www.iso.org/obp/ui/#iso:std:iso:19107:ed-2:v1:en'

response = session.get(url)
print(response.status_code) # Si retourne 200 = OK
# Execution du Javascript
response.html.render(sleep=1, keep_page=True)

ISODico = jsonreading.readJsonFileViz('data.json')

# Parsing
# Récupération de le liste des noms et liens de normes présent dans le documents
StandListSTDNotClean = response.html.find('.sts-std-ref')
if not StandListSTDNotClean:
    StandListXREFNotClean = response.html.find('li')
for text in StandListXREFNotClean:
    ISONameXREF = unicodedata.normalize("NFKD",text.text)
    if ISONameXREF.startswith('—') == False and "Annex" not in ISONameXREF: # Test obligatoire sinon je récupère d'autres listes sur certaines normes / J'ai rajouté un test pour ne pas avoir le lien des annexes
        ISONameXREFSplit = ISONameXREF.split(",")
        print(ISONameXREFSplit[0])
        print(filter(lambda item: item[ISONameXREFSplit], ISODico))
# Récupération des normes présentes mais qui n'était pas encore publiée lors de la soumission de la norme

FindStandNum = response.html.find('.v-label-h2')
ISOName = unicodedata.normalize("NFKD",FindStandNum[0].text)
ISOName = ISOName.split(" ")
if '-' in ISOName[1]:
    ISONum = ISOName[1].split("-")
else:
    ISONum = ISOName[1].split(":")
print(ISONum)
StandListSTDToClean = response.html.find('.sts-std-ref',containing=ISONum[0])

####TEST PART POUR XREF ####
#TODO si fonctionne faire une fonction si c'est plus simple
StandListListXREFToClean = response.html.find('li',containing=ISONum[0])
for element in StandListListXREFToClean:
    for element2 in StandListXREFNotClean:
        if element.absolute_links == element2.absolute_links or "Guide" in element2.text:
            StandListXREFNotClean.remove(element2)
StandListXREFClean = StandListXREFNotClean

#Maintenant on vient vraiment nettoyer les liens
for element in StandListSTDToClean:
    for element2 in StandListSTDNotClean:
        if element.absolute_links == element2.absolute_links or "Guide" in element2.text:
            StandListSTDNotClean.remove(element2)
StandListSTDClean = StandListSTDNotClean

print(StandListSTDClean)
for element3 in StandListSTDClean:
    print(element3)
    for link in element3.absolute_links:
        print(type(link))
        print(link)
    
    #print(element3.text)

# for element4 in StandListXREFClean:
#     print(element3.absolute_links)