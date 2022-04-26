import pandas as pd
from pandas import json_normalize
import numpy as np
from jsonreading import readJsonFileViz

import warnings

warnings.filterwarnings("ignore")

import holoviews as hv

#Convertir mon fichier json en Dataframe
##Solution 1 (json_normalize):
ISODico = readJsonFileViz("data.json")
#df = json_normalize(ISODico)
#print(df)
##Solution 2 (readjson)
#links = pd.read_json("data.json", orient='index')
#print(links.head())



############################################################################################
#Voici ma liste de normes
ISOList = []
for key in ISODico.keys():
    ISOList.append(ISODico[key]["short"])


# linkslist = ISODico["https://www.iso.org/obp/ui/#iso:std:iso:19136:-2:en"]["dependance"]
# # print(linkslist)
# print(linkslist.count("https://www.iso.org/obp/ui/#iso:std:iso:19108:en"))

# #Besoin d'un liste de couple url_src url_dest et d'un count pour le nombre de fois
# coupleList = []
# for key in ISODico.keys():
#     for link in ISODico[key]["dependance"]:
#         coupleList.append([ISODico[key]["short"],ISODico[link]["short"],ISODico[key]["dependance"].count(link)])
# # print(coupleList)

#Affichage du diagramme de dépendance
# chord = hv.Chord((coupleList,ISOList))
# chord.opts(
#     opts.Chord(node_color="ISO", node_cmap="Category20", cmap='Category20', edge_cmap='Category20', 
#                labels='ISO', edge_line_width=2, height=500, width=500, title="ISO 19100 series dependancies", hooks=[rotate_label]))


# def rotate_label(plot, element):
#     white_space = "                  "
#     angles = plot.handles['text_1_source'].data['angle']
#     characters = np.array(plot.handles['text_1_source'].data['text'])
#     plot.handles['text_1_source'].data['text'] = np.array([x + white_space if x in characters[np.where((angles < -1.5707963267949) | (angles > 1.5707963267949))] else x for x in plot.handles['text_1_source'].data['text']])
#     plot.handles['text_1_source'].data['text'] = np.array([white_space + x if x in characters[np.where((angles > -1.5707963267949) | (angles < 1.5707963267949))] else x for x in plot.handles['text_1_source'].data['text']])
#     angles[np.where((angles < -1.5707963267949) | (angles > 1.5707963267949))] += 3.1415926535898
#     plot.handles['text_1_glyph'].text_align = "center"