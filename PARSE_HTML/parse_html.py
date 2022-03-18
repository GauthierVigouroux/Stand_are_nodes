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
    StandListSTD = response.html.find('.sts-std-ref')
    # Récupération des normes présentes mais qui n'était pas encore publiée lors de la soumission de la norme
    StandListXREF = response.html.find('li')
    #On vient remplire les dico

    for element in StandListXREF:
        if str(element.text).startswith('—') == False: # Test obligatoire sinon je récupère d'autres listes sur certaines normes
            ISODict[str(element.text).split(',',1)[0]] = [str(element.text),None,tuple()] # Pour modifier le tuple il faut retransformer en liste (les listes ne sont pas hasables)
    # Afin d'être le plus précis possible je dois regarder au delas des références normatives
    # et prendre en compte .
    for item in StandListSTD:
        if str(item.text).startswith('—') == False:
            ISODict[str(item.text).split(',',1)[0]] = [str(item.text),str(item.absolute_links),tuple()]
    # Print Testing
    for cle in ISODict.keys():
        print(cle)
    # Trouver un moyen d'afficher le dico pour vérifier
    return ISODict



#isorequests('https://www.iso.org/obp/ui/fr/#iso:std:iso:19108:ed-1:v1:en')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-1:ed-1:v1:fr')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:fr')