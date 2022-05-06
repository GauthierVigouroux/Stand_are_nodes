from cgitb import html
import pandas as pd
import numpy as np
from jsonreading import readJsonFileViz
import math
import statistics

import warnings

warnings.filterwarnings("ignore")

import holoviews as hv

#Convertir mon fichier json en Dataframe
##Solution 1 (json_normalize):
ISODico = readJsonFileViz("data.json")
#df = json_normalize(ISODico)
#print(df)
##Solution 2 (readjson)
# links = pd.read_json("data.json", orient='index')
# print(links.head())


sourcelist = list()
targetlist = list()
valuelist = list()

T=0
for i in ISODico.keys():
    for k in ISODico[i]["dependance"]:
        T+=len(k)

for key in ISODico.keys():
    for iso in ISODico[key]["dependance"]:
        if not(ISODico[key]["dependance"]) == False:
            sourcelist.append(ISODico[key]["short"])
            targetlist.append(ISODico[iso]["short"])
            tf_ref = ISODico[key]["dependance"].count(iso)
            sf_ref = ISODico[iso]["global_count_citation"]
            isf_ref = math.log(len(ISODico.keys())/sf_ref)
            w = tf_ref * isf_ref
            valuelist.append(w)
source = pd.DataFrame(sourcelist)
target = pd.DataFrame(targetlist)
value = pd.DataFrame(valuelist)

# Calcul du poid moyen :
print("La moyenne du poid est de : " + str(statistics.mean(valuelist)))
print("L'écart type est de : " + str(statistics.pstdev(valuelist)))

links = pd.concat([source, target, value], axis=1)
links.columns = ['source', 'target', 'value']
print(links.head())

#Voici ma liste de normes
ISOListlien =list()
ISOListnom = list()
for key in ISODico.keys():
#    ISOListlien.append(key)
    ISOListnom.append(ISODico[key]["short"])
#ISOListlien = pd.DataFrame(ISOListlien)
# ISOListnom = pd.DataFrame(ISOListnom)
# ISODataFrame = pd.concat([ISOListnom],axis=1)
ISODataSet = hv.Dataset(pd.DataFrame(ISOListnom,columns=["ISO"]))
# Filtrage sur le nombre de référence minimum
min_nav = 6.5
hv.extension('bokeh')
chord = hv.Chord((links, ISODataSet)).select(value=(min_nav, None))




############################################################################################
          
def rotate_label(plot, element):
    white_space = "                  "
    angles = plot.handles['text_1_source'].data['angle']
    characters = np.array(plot.handles['text_1_source'].data['text'])
    plot.handles['text_1_source'].data['text'] = np.array([x + white_space if x in characters[np.where((angles < -1.5707963267949) | (angles > 1.5707963267949))] else x for x in plot.handles['text_1_source'].data['text']])
    plot.handles['text_1_source'].data['text'] = np.array([white_space + x if x in characters[np.where((angles > -1.5707963267949) | (angles < 1.5707963267949))] else x for x in plot.handles['text_1_source'].data['text']])
    angles[np.where((angles < -1.5707963267949) | (angles > 1.5707963267949))] += 3.1415926535898
    plot.handles['text_1_glyph'].text_align = "center"

# linkslist = ISODico["https://www.iso.org/obp/ui/#iso:std:iso:19136:-2:en"]["dependance"]
# # print(linkslist)
# print(linkslist.count("https://www.iso.org/obp/ui/#iso:std:iso:19108:en"))

# #Comptage du nombre de liens présent pour notre column valeur 
# coupleList = []
# for key in ISODico.keys():
#     for link in ISODico[key]["dependance"]:
#         coupleList.append([ISODico[key]["short"],ISODico[link]["short"],ISODico[key]["dependance"].count(link)])
# # print(coupleList)

#Affichage du diagramme de dépendance
# chord = hv.Chord((coupleList,ISOList))
chord.opts(node_color="ISO", node_cmap="Category20", cmap='Category20', edge_cmap='Category20', edge_color="source",
               labels='ISO', edge_line_width=2, height=1500, width=1500, title="ISO 19100 Series", hooks=[rotate_label])

hv.save(chord, 'chordviz.html',fmt='html')