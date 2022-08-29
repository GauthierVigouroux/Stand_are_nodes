import unicodedata
from requests_html import HTMLSession
import re

# Html retrieval and parsing function
def isorequests(url,ISODict):
    # Dictionary format
    # ISODict[str]=[str,str,tuple]

    # Initialization of the session
    session = HTMLSession()
    
    # Recovery of the source code
    response = session.get(url)
    #Quick test to see if there is an error at a given time
    if response.status_code != 200:
        print(response.status_code)
    
    # Javascripts Execution
    response.html.render(sleep=1, keep_page=True)

    # Parsing
    # Retrieving the list of names and links of standards in the document
    StandListSTDNotClean = response.html.find('.sts-std-ref')
    # If the standard's references are not populated with links, the name must be retrieved
    if not StandListSTDNotClean:
        StandListXREF = response.html.find('li')
        for element in StandListXREF:
            ISONameXREF = unicodedata.normalize("NFKD",element.text)
            if ISONameXREF.startswith('—') == False and "Annex" not in ISONameXREF: # Mandatory test otherwise I get other lists on some standards / I added a test to not have the link of the annexes
                print()
                ISONameXREFSplit = ISONameXREF.split(",")


    # Retrieval of standards that were present but not yet published when the standard was submitted
    #StandListXREF = response.html.find('li')
    

    #Cleaning of the links with those that point to the questioned link (the points where there is a reference to the analysed standard)
    #Retrieving the standard number
    FindStandNum = response.html.find('.v-label-h2')
    ISOName = unicodedata.normalize("NFKD",FindStandNum[0].text).replace('(en)','')
    ISONameSplit = ISOName.split(" ")
    if '-' in ISONameSplit[1]:
        ISONum = ISONameSplit[1].split("-")
    else:
        ISONum = ISONameSplit[1].split(":")
    StandListSTDToClean = response.html.find('.sts-std-ref',containing=ISONum[0])
    #Retrieving the name of the standard
    # FindStandName = response.html.find('.std-title')
    # StandName = FindStandName[0].text
    #Now we really come to clean the links
    for element in StandListSTDToClean:
        for element2 in StandListSTDNotClean:
            if element.absolute_links == element2.absolute_links or "Guide" in element2.text:
                StandListSTDNotClean.remove(element2)
    StandListSTDClean = StandListSTDNotClean

    #The dictionaries are filled with new standards (we have a dictionary so normally the data will not be duplicated)
    #DONE Whether it is a Guide standard or not (ref above)
    # for element in StandListXREF:
    #     print(element.absolute_links)
    #     if str(element.text).startswith('—') == False and "Annex" not in element.text: # Mandatory test otherwise I get other lists on some standards / I added a test to not have the link of the annexes.
    #         ISODict[unicodedata.normalize("NFKD",str(element.text).split(',',1)[0])] = [unicodedata.normalize("NFKD",str(element.text)),None,tuple()] # To modify the tuple you have to transform it back into a list (lists are not hashable)
    # In order to be as accurate as possible I have to look beyond the normative references and take into account .

    # linktuple = tuple()
    for item in StandListSTDClean:
        #print(item.absolute_links)
        #Some items that start with -- are not links to standards.
        if item.text.startswith('—') == False or item.text.startswith('ISO') == False:
            # for value in item.absolute_links:
            #     link = value
            #     print(link)
            # linktuple = linktuple + (link,)
            #Test if the key exists in the dictionary so as not to rewrite over it
                        #In order to have the same links and not to have several nodes for the same key, the 'ed-1' and 'v1' must be removed from the links
            linkform = ''.join(item.absolute_links)
            linkform = re.sub("ed-1:|ed-2:|ed-3:|ed-4:|ed-5:|v1:|v2:|v3:|v4:","",linkform)
            #To clean it up again, we split to remove what would be behind the ':en', we take the separator ":clause" which is always behind the ":en".
            linkform = linkform.split(":clause")
            if linkform[0] not in ISODict:
                print("Nouvelle clé")
                # ISODict[unicodedata.normalize("NFKD",str(item.text).split(',',1)[0])] = {
                #     "nom":unicodedata.normalize("NFKD",str(item.text)),
                #     "lien":re.sub("ed-1:|ed-2:|ed-3:|ed-4:|ed-5:|v1:|v2:|v3:|v4:","",(''.join(item.absolute_links.pop()))).split(":clause")[0],
                #     "dependance":[]
                #     }                
                ISODict[re.sub("ed-1:|ed-2:|ed-3:|ed-4:|ed-5:|v1:|v2:|v3:|v4:","",(''.join(item.absolute_links.pop()))).split(":clause")[0]] = {
                    "short":unicodedata.normalize("NFKD",str(item.text).split(',',1)[0]),
                    "nom":unicodedata.normalize("NFKD",str(item.text)),
                    "dependance":[],
                    "global_count_citation":0
                }
            #Then we come and fill in the dictionary
            ISODict[url]["dependance"].append(linkform[0])
    # Print Testing
    #for cle in ISODict.keys():
        #print(cle)


    return ISODict



#isorequests('https://www.iso.org/obp/ui/fr/#iso:std:iso:19108:ed-1:v1:en')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-1:ed-1:v1:fr')
#isorequests('https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:fr')