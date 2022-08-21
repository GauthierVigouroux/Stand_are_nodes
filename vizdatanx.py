from pyvis.network import Network
import jsonreading
import math
import networkx as nx

#Initialisation
Dicoviz = jsonreading.readJsonFileViz("data.json")
DicoInit = jsonreading.readJsonFileInit("isolist_v3.json")
nx_graph = nx.Graph()

for key in Dicoviz.keys():
    value = len(Dicoviz[key]["dependance"])
    if Dicoviz[key]["short"].startswith("ISO/IEC"):
        nx_graph.add_node(key,label=Dicoviz[key]["short"], color="#03DAC6", value=value*100000)
    elif "TS" in Dicoviz[key]["short"]:
        nx_graph.add_node(key,label=Dicoviz[key]["short"],color="#da03b3", value=value*100000)
    elif key in DicoInit.keys():
        nx_graph.add_node(key,label=Dicoviz[key]["short"],color="#FFFF00", value=value*100000)
    else:
        nx_graph.add_node(key,label=Dicoviz[key]["short"], value=value*100000)

T=0
for i in Dicoviz.keys():
    for k in Dicoviz[i]["dependance"]:
        T+=len(k)
print("Nombre totale de références dans l'écosystème : " + str(T))
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
        try:
            nx_graph.add_edge(url_src,url_dest[i],color="#018786", value = w)
            print()
        except KeyError as e:
            nx_graph.add_node(url_dest[i])
            nx_graph.add_edge(url_src,url_dest[i],color="#018786", value = w)
            # print(e)
        except AssertionError as e:
            nx_graph.add_node(url_dest[i])
            nx_graph.add_edge(url_src,url_dest[i],color="#018786", value = w)
            # print(e)

