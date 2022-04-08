import unicodedata
from requests_html import HTMLSession

# Fonction de récupération et de parsing de l'html
def isorequests(url,ISODict):
    # Format du dico
    # ISODict[str]=[str,str,tuple]

    # Initialisation de la session
    session = HTMLSession()
    
    # Récupération du code source
    response = session.get(url)
    print(response.status_code) # Si retourne 200 = OK
    
    # Execution du Javascript
    response.html.render(sleep=1, keep_page=True)

    # Parsing
    # Récupération de le liste des noms et liens de normes présent dans le documents
    StandListSTDNotClean = response.html.find('.sts-std-ref')
    # Récupération des normes présentes mais qui n'était pas encore publiée lors de la soumission de la norme
    #StandListXREF = response.html.find('li')
    

    #Nettoyage des liens avec ceux qui repointes vers le lien interrogé
    #Récupération du numéro de la norme
    FindStandNum = response.html.find('.v-label-h2')
    ISOName = unicodedata.normalize("NFKD",FindStandNum[0].text)
    ISOName = ISOName.split(" ")
    if '-' in ISOName[1]:
        ISONum = ISOName[1].split("-")
    else:
        ISONum = ISOName[1].split(":")
    StandListSTDToClean = response.html.find('.sts-std-ref',containing=ISONum[0])
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
    for item in StandListSTDClean:
        #print(item.absolute_links)
        if str(item.text).startswith('—') == False:
            print(type(item.absolute_links))
            ISODict[unicodedata.normalize("NFKD",str(item.text).split(',',1)[0])] = [unicodedata.normalize("NFKD",str(item.text)),str(item.absolute_links),tuple()]
    # Print Testing
    #for cle in ISODict.keys():
        #print(cle)
    #TODO Alimenter le dico en liens


    return ISODict



#isorequests('https://www.iso.org/obp/ui/fr/#iso:std:iso:19108:ed-1:v1:en')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-1:ed-1:v1:fr')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:fr')