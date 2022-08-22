
from pyvis.network import Network
import jsonreading
import math

#Initialisation
Dicoviz = jsonreading.readJsonFileViz("data.json")
iso_net = Network(height='1500px', width='100%',font_color='black',directed=True, neighborhood_highlight=True) #select_menu=True
# iso_net = Network(height='1500px', width='75%',font_color='black',directed=True)

DicoInit = jsonreading.readJsonFileInit("isolist_v3.json")

#Alimentation du réseau
##Création des nodes
for key in Dicoviz.keys():
    value = len(Dicoviz[key]["dependance"])
    if Dicoviz[key]["short"].startswith("ISO/IEC"):
        # iso_net.add_node(key,label=Dicoviz[key]["short"], color="#03DAC6", value=value)
        iso_net.add_node(key,label=Dicoviz[key]["short"], value=value) #value=value
    elif "TS" in Dicoviz[key]["short"]:
        # iso_net.add_node(key,label=Dicoviz[key]["short"],color="#da03b3", value=value)
        iso_net.add_node(key,label=Dicoviz[key]["short"], value=value)
    elif key in DicoInit.keys():
        # iso_net.add_node(key,label=Dicoviz[key]["short"],color="#FFFF00", value=value)
        iso_net.add_node(key,label=Dicoviz[key]["short"], value=value)
    else:
        iso_net.add_node(key,label=Dicoviz[key]["short"], value=value)
    

T=0
for i in Dicoviz.keys():
    for k in Dicoviz[i]["dependance"]:
        T+=len(k)

depend_counter=0

##Creation des edges avec gestions des exceptions
for key in Dicoviz.keys():
    url_src = key
    url_dest = Dicoviz[key]["dependance"]
    depend_counter = len(url_dest) + depend_counter
    #Calcul du poid des edges
    ##T = Nombre totale de références dans l'écosystème
    ##tf_ref = Fréquence de la référence dans la norme s >> Dicoviz[key]["dependance"].count(url_dest)
    

    for i in range(len(url_dest)):
        tf_ref = Dicoviz[key]["dependance"].count(url_dest[i])
        sf_ref = Dicoviz[url_dest[i]]["global_count_citation"]
        isf_ref = math.log(len(Dicoviz.keys())/(sf_ref+1))
        w = tf_ref * isf_ref
        value_nodes = len(Dicoviz[key]["dependance"])
        try:
            #iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
            iso_net.add_edge(url_src,url_dest[i], value = w)
        except KeyError as e:
            iso_net.add_node(url_dest[i], value = value_nodes)
            #iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
            iso_net.add_edge(url_src,url_dest[i], value = w)
            # print(e)
        except AssertionError as e:
            iso_net.add_node(url_dest[i], value = value_nodes)
            #iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
            iso_net.add_edge(url_src,url_dest[i], value = w)
            # print(e)

#gère l'affichage des boutons
buttons=True
if buttons==True:
  iso_net.width="75%"
  iso_net.show_buttons()
  iso_net.force_atlas_2based()
else:  
  iso_net.set_options("""
  var options = {
    "nodes": {
      "borderWidthSelected": 6,
      "color": {
        "highlight": {
          "border": "rgba(233,34,61,1)",
          "background": "rgba(210,229,255,1)"
        }
      }
    },
    "edges": {
      "arrows": {
        "to": {
          "enabled": true,
          "scaleFactor": 0.3
        }
      },
      "color": {
        "highlight": "rgba(255,19,34,1)",
        "inherit": false
      },
      "smooth": false
    },
  "physics": {
    "forceAtlas2Based": {
      "springLength": 100
    },
    "minVelocity": 0.75,
    "solver": "forceAtlas2Based"
  }
  }
  """)

#Utilisation et personalisation de barnes_hut
#iso_net.barnes_hut(gravity=-8300,central_gravity=0,spring_length=435,spring_strength=0.04,damping=0.4,overlap=0.9)
# # iso_net.set_options("""var options = {
#   "nodes": {
#     "color": {
#       "highlight": {
#         "border": "rgba(24,255,22,1)"
#       }
#     }
#   },
#   "edges": {
#     "color": {
#       "highlight": "rgba(255,21,12,1)",
#       "inherit": false
#     },
#     "smooth": {
#       "type": "continuous",
#       "forceDirection": "none",
#       "roundness": 0.75
#     },
#     "width": 30
#   },
#   "physics": {
#     "barnesHut": {
#       "gravitationalConstant": -9150,
#       "centralGravity": 2.85,
#       "springLength": 250,
#       "springConstant": 0.001
#     },
#     "minVelocity": 0.75
#   }
# }
# """)

#iso_net.toggle_hide_nodes_on_drag(True)
#Affichage du réseau
#Désactiovation dans le doutes mais je ne sais pas si cela affectera le graph pour l'instant.
#iso_net.toggle_physics(True)
print(depend_counter)
iso_net.show("iso_net.html")