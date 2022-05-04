from unicodedata import name
from requests_html import HTMLSession

def get_name_short_status(link):

    name_short_status = dict()
    session_recup = HTMLSession()
    response = session_recup.get(link)
    if response.status_code != 200:
        print("Echec de la récupération du nom")
        print(response.status_code)
    response.html.render(sleep=1, keep_page=True)
    isoshort = response.html.find('.h2',first=True)
    isoname = response.html.find('.v-slot-std-title',first=True)
    status = response.html.find('.std-alert-warning',first=True)
    print(link)
    if status :
        status_code = "Updated"
    else :
        status_code = "Deprecated"
    if isoshort is None :
        name_short_status = {
            "short": None,
            "name": None,
            "status": None
        }
    else :
        name_short_status = {
        # Voir pour enlever le (en) pour faire propre
            "short":isoshort.text,
            "name":isoname.text,
            "status":status_code
        }

    return name_short_status

def isorequests(url,ISODict):

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
    divScope = response.html.find('div[id$="sec_1"]',first=True)
    divNormRef = response.html.find('div[id$="sec_3"]',first=True)

    # Récupération des dépendances présentent
    if divScope :
        ScopeDep = divScope.absolute_links
    else :
        ScopeDep = set()
    # Je vais peut être devoir rendre moins cassant cette partie
    NormeDep = divNormRef.absolute_links
    # On forme un seul set
    ScopeDep.update(NormeDep)
    Dependencies = ScopeDep

    # Récupération des noms et liens de normes si non présent dans le dico
    for links in Dependencies:
        # Test si il y a un # dans les liens, il y en a un peu partout dans le code
        bad_link = False
        if "#"  in links:
            
            links = links.split(":term")
            links = links[0]

            if links not in ISODict.keys():
                iso_name_and_short = get_name_short_status(links)
                ISODict[links] = {
                    "short": iso_name_and_short["short"],
                    "nom": iso_name_and_short["name"],
                    "dependance":{},
                    "status":iso_name_and_short["status"]
                }
            # Alimentation des dépendances
            ISODict[url]["dependance"][links] = {
                "citation_int" : int
            }
        else :
            bad_link = True

    # Si le test précédent est vrai alors on skip
    if bad_link == False :
        # Nombre de fois cité dans le document
        # On recupère une nouvelle fois les liens pour ne pas avoir la forme absolue
        ScopeDep = divScope.links
        NormeDep = divNormRef.links
        ScopeDep.update(NormeDep)
        # Transformation en liste pour pouvoir parcourir
        citations = []
        for element in ScopeDep:
            citations.append(element)
    
    # On cherche combien de fois la dépendance est cité dans le document
        for href in citations:
            if "#" in href:
                citation_int = 0
                find = "a[href="+ href +"]"
                for element in response.html.find('a',containing=href):
                    citation_int += 1
                links = "https://www.iso.org/obp/ui/" + href
                links = links.split(":term")
                links = links[0]
                ISODict[url]["dependance"][links]["citation_int"] = citation_int

    return ISODict