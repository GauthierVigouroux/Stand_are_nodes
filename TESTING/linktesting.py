from shutil import ExecError
import unicodedata
from requests_html import HTMLSession

session = HTMLSession()
url = 'https://www.iso.org/obp/ui/fr/#iso:std:iso:19104:ed-1:v1:en'

response = session.get(url)
print(response.status_code) # Si retourne 200 = OK
# Execution du Javascript
response.html.render(sleep=1, keep_page=True)

# Parsing
# Récupération de le liste des noms et liens de normes présent dans le documents
StandListSTDNotClean = response.html.find('.sts-std-ref')
# Récupération des normes présentes mais qui n'était pas encore publiée lors de la soumission de la norme
StandListXREFNotClean = response.html.find('li')

FindStandNum = response.html.find('.v-label-h2')
ISOName = unicodedata.normalize("NFKD",FindStandNum[0].text)
ISOName = ISOName.split(" ")
if '-' in ISOName[1]:
    ISONum = ISOName[1].split("-")
else:
    ISONum = ISOName[1].split(":")
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

for element3 in StandListSTDClean:
    print(element3.absolute_links)
    #print(element3.text)

# for element4 in StandListXREFClean:
#     print(element3.absolute_links)