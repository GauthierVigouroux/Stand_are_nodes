import unicodedata
from requests_html import HTMLSession
import re

# Fonction de récupération et de parsing de l'html
def isorequests(url,ISODict):
    # Format du dico
    # ISODict[str]=[str,str,tuple]

    # Initialisation de la session
    session = HTMLSession()
    
    # Récupération du code source
    response = session.get(url)
    #Test rapide pour savoir si il y a une erreure à un moment donné
    if response.status_code != 200:
        print(response.status_code)
    
    # Execution du Javascript
    response.html.render(sleep=1, keep_page=True)

    # Parsing
    # Récupération de le liste des noms et liens de normes présent dans le documents
    StandListSTDNotClean = response.html.find('.sts-std-ref')
    # Si les références de la norme ne sont pas alimenté en liens il faut récupérer le nom
    if not StandListSTDNotClean:
        StandListXREF = response.html.find('li')
        for element in StandListXREF:
            ISONameXREF = unicodedata.normalize("NFKD",element.text)
            if ISONameXREF.startswith('—') == False and "Annex" not in ISONameXREF: # Test obligatoire sinon je récupère d'autres listes sur certaines normes / J'ai rajouté un test pour ne pas avoir le lien des annexes
                print()
                ISONameXREFSplit = ISONameXREF.split(",")


    # Récupération des normes présentes mais qui n'était pas encore publiée lors de la soumission de la norme
    #StandListXREF = response.html.find('li')
    

    #Nettoyage des liens avec ceux qui repointes vers le lien interrogé (Les points où il y a ref a la norme analysé)
    #Récupération du numéro de la norme
    FindStandNum = response.html.find('.v-label-h2')
    ISOName = unicodedata.normalize("NFKD",FindStandNum[0].text).replace('(en)','')
    ISONameSplit = ISOName.split(" ")
    if '-' in ISONameSplit[1]:
        ISONum = ISONameSplit[1].split("-")
    else:
        ISONum = ISONameSplit[1].split(":")
    StandListSTDToClean = response.html.find('.sts-std-ref',containing=ISONum[0])
    #Récupération du nom de la norme
    # FindStandName = response.html.find('.std-title')
    # StandName = FindStandName[0].text
    #Maintenant on vient vraiment nettoyer les liens
    for element in StandListSTDToClean:
        for element2 in StandListSTDNotClean:
            if element.absolute_links == element2.absolute_links or "Guide" in element2.text:
                StandListSTDNotClean.remove(element2)
    StandListSTDClean = StandListSTDNotClean

    #On vient remplire les dico de nouvelles normes(On a un dico donc normalement les données ne seront pas dupliqués)
    #DONE Si ce n'est pas une norme Guide ou non (ref en haut)
    # for element in StandListXREF:
    #     print(element.absolute_links)
    #     if str(element.text).startswith('—') == False and "Annex" not in element.text: # Test obligatoire sinon je récupère d'autres listes sur certaines normes / J'ai rajouté un test pour ne pas avoir le lien des annexes
    #         ISODict[unicodedata.normalize("NFKD",str(element.text).split(',',1)[0])] = [unicodedata.normalize("NFKD",str(element.text)),None,tuple()] # Pour modifier le tuple il faut retransformer en liste (les listes ne sont pas hasables)
    # Afin d'être le plus précis possible je dois regarder au delas des références normatives
    # et prendre en compte .

    # linktuple = tuple()
    for item in StandListSTDClean:
        #print(item.absolute_links)
        #Certains items qui commencent par -- ne sont pas des liens vers des normes.
        if item.text.startswith('—') == False:
            # for value in item.absolute_links:
            #     link = value
            #     print(link)
            # linktuple = linktuple + (link,)
            #Test si la clé existe dans le dico afin de ne pas rewrite par dessus
            if unicodedata.normalize("NFKD",str(item.text).split(',',1)[0]) not in ISODict:
                print("Nouvelle clé")
                ISODict[unicodedata.normalize("NFKD",str(item.text).split(',',1)[0])] = {
                    "nom":unicodedata.normalize("NFKD",str(item.text)),
                    "lien":re.sub("ed-1:|ed-2:|ed-4:|ed-5:|v1:|v2:|v3:|v4:","",(''.join(item.absolute_links.pop()))),
                    "dependance":[]
                    }
            #Afin d'avoir les mêmes liens et ne pas avoir plusieurs nodes pour la même clé il faut retirer les 'ed-1' et 'v1' des liens
            linkform = ''.join(item.absolute_links)
            linkform = re.sub("ed-1:|ed-2:|ed-4:|ed-5:|v1:|v2:|v3:|v4:","",linkform)
            #Ensuite on vient remplire le dico
            ISODict[ISOName]["dependance"].append(linkform)
    # Print Testing
    #for cle in ISODict.keys():
        #print(cle)
    #TODO Alimenter le dico en liens


    return ISODict



#isorequests('https://www.iso.org/obp/ui/fr/#iso:std:iso:19108:ed-1:v1:en')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-1:ed-1:v1:fr')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:fr')