from requests_html import HTMLSession

# Fonction de récupération et de parsing de l'html
def isorequests(url):

    # Initialisation de la session
    session = HTMLSession()
    
    # Récupération du code source
    response = session.get(url)
    print(response.status_code) # Si retourne 200 = OK
    
    # Execution du Javascript
    response.html.render(sleep=1, keep_page=True)

    # Parsing
    # Récupération de le liste des noms de norme
    StandListAllDoc = response.html.find('.sts-section .sts-ref-list', first=True)
    # On clean la liste des différents lien qu'il y a en trop
    StandList = StandListAllDoc.html.find('a.sts-std-ref')

    # Print Testing
    for item in StandList :
        print(item.text)