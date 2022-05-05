
from pyvis.network import Network
import jsonreading
import math

#Initialisation
Dicoviz = jsonreading.readJsonFileViz("data.json")
iso_net = Network(height='1500px', width='75%',font_color='black',directed=True,)
DicoInit = jsonreading.readJsonFileInit("isolist_v3.json")

#Alimentation du réseau
##Création des nodes
for key in Dicoviz.keys():
    value = len(Dicoviz[key]["dependance"])
    if Dicoviz[key]["short"].startswith("ISO/IEC"):
        iso_net.add_node(key,label=Dicoviz[key]["short"], color="#03DAC6", value=value*100000)
    elif "TS" in Dicoviz[key]["short"]:
        iso_net.add_node(key,label=Dicoviz[key]["short"],color="#da03b3", value=value*100000)
    elif key in DicoInit.keys():
        iso_net.add_node(key,label=Dicoviz[key]["short"],color="#FFFF00", value=value*100000)
    else:
        iso_net.add_node(key,label=Dicoviz[key]["short"], value=value*100000)
    

T=0
for i in Dicoviz.keys():
    for k in Dicoviz[i]["dependance"]:
        T+=len(k)

##Creation des edges avec gestions des exceptions
for key in Dicoviz.keys():
    url_src = key
    url_dest = Dicoviz[key]["dependance"]

    #Calcul du poid des edges
    ##T = Nombre totale de références dans l'écosystème
    ##tf_ref = Fréquence de la référence dans la norme s >> Dicoviz[key]["dependance"].count(url_dest)
    

    for i in range(len(url_dest)):
        tf_ref = Dicoviz[key]["dependance"].count(url_dest[i])
        sf_ref = Dicoviz[url_dest[i]]["global_count_citation"]
        isf_ref = math.log(len(Dicoviz.keys())/sf_ref)
        w = tf_ref * isf_ref
        value_nodes = len(Dicoviz[key]["dependance"])
        try:
            iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
            print()
        except KeyError as e:
            iso_net.add_node(url_dest[i], value = value_nodes)
            iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
            # print(e)
        except AssertionError as e:
            iso_net.add_node(url_dest[i], value = value_nodes)
            iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
            # print(e)

#Utilisation d'algo
iso_net.show_buttons()
iso_net.barnes_hut(gravity=-8300,central_gravity=0,spring_length=435,spring_strength=0.04,damping=0.4,overlap=0.9)

#Affichage du réseau
iso_net.toggle_physics(True)
iso_net.show("iso_net.html")