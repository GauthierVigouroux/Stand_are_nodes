from pyvis.network import Network
import jsonreading

#Initialisation
Dicoviz = jsonreading.readJsonFileViz("data.json")
iso_net = Network(height='1500px', width='100%', bgcolor='#222222',font_color='white')
DicoInit = jsonreading.readJsonFileInit("isolist_v3.json")

#Alimentation du réseau
##Création des nodes
for key,value in Dicoviz.items():
    if Dicoviz[key]["short"].startswith("ISO/IEC"):
        iso_net.add_node(key,label=Dicoviz[key]["short"], color="#03DAC6")
    elif "TS" in Dicoviz[key]["short"]:
        iso_net.add_node(key,label=Dicoviz[key]["short"],color="#da03b3")
    elif key in DicoInit.keys():
        iso_net.add_node(key,label=Dicoviz[key]["short"],color="#FFFF00",shape="star")
    else:
        iso_net.add_node(key,label=Dicoviz[key]["short"])
    

##Creation des edges avec gestions des exceptions
for key,value in Dicoviz.items():
    url_src = key
    url_dest = Dicoviz[key]["dependance"]
    for i in range(len(url_dest)):
        try:
            iso_net.add_edge(url_src,url_dest[i],color="#018786")
            print()
        except KeyError as e:
            iso_net.add_node(url_dest[i])
            iso_net.add_edge(url_src,url_dest[i],color="#018786")
            # print(e)
        except AssertionError as e:
            iso_net.add_node(url_dest[i])
            iso_net.add_edge(url_src,url_dest[i],color="#018786")
            # print(e)

#Utilisation d'algo
iso_net.barnes_hut()

#Affichage du réseau
iso_net.toggle_physics(True)
iso_net.show("iso_net.html")