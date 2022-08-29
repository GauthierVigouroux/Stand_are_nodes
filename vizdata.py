
from pyvis.network import Network
import jsonreading
import math
import sys, getopt, operator
import networkx as nx

# Command Line Arguments
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -b <basefile> -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in("-b", "--bfile"):
            basefile = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    #Initialisation
    Dicoviz = jsonreading.readJsonFileViz("databases/" + inputfile)
    iso_net = Network(neighborhood_highlight=True, select_menu=True,directed=True) # notebook=True, 
    DicoInit = jsonreading.readJsonFileInit("databases/" + basefile)
    iso_nx = nx.DiGraph()

    #Alimentation du réseau
    #Ajout des noeuds
    for key in Dicoviz.keys():
        value = len(Dicoviz[key]["dependance"])
        iso_nx.add_node(key)
        
    #Partie pour l'intialisation au calcul de poid
    T=0
    for i in Dicoviz.keys():
        for k in Dicoviz[i]["dependance"]:
            T+=len(k)

    ##Creation des edges avec gestions des exceptions
    for key in Dicoviz.keys():
        src = key
        url_dest = Dicoviz[key]["dependance"]
            
        #Calcul du poid des edges
        ##T = Nombre totale de références dans l'écosystème
        ##tf_ref = Fréquence de la référence dans la norme s >> Dicoviz[key]["dependance"].count(url_dest)
        

        for i in range(len(url_dest)):
            tf_ref = Dicoviz[key]["dependance"].count(url_dest[i])
            sf_ref = Dicoviz[url_dest[i]]["global_count_citation"]+1
            isf_ref = math.log(len(Dicoviz.keys())/sf_ref)
            w = tf_ref * isf_ref
            value_nodes = len(Dicoviz[key]["dependance"])        
            try:
                #iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
                iso_nx.add_edge(src,url_dest[i], weight = w)
                #iso_nx.nodes[key]['weight']=w
                iso_nx.nodes[key]['size']=len(Dicoviz[src]["dependance"])
            except KeyError as e:
                iso_nx.add_node(url_dest[i],size=len(Dicoviz[url_dest]["dependance"]))
                #iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
                iso_nx.add_edge(src,url_dest[i], weight = w)
                # print(e)
            except AssertionError as e:
                iso_nx.add_node(url_dest[i],size=len(Dicoviz[url_dest]["dependance"]))
                #iso_net.add_edge(url_src,url_dest[i],color="#018786", value = w)
                iso_nx.add_edge(src,url_dest[i], weight = w)
                # print(e) 

    ##sourcealgo : https://networkx.org/documentation/stable/reference/algorithms/index.html
    #nx.betweenness_centrality(iso_nx)
    #############
    #rgb_to_hex((255, 255, 195))
    nx.degree_centrality(iso_nx)

    degree_centrality = nx.in_degree_centrality(iso_nx)
    max_key = max(degree_centrality, key=lambda key: degree_centrality[key])
    max_degree = degree_centrality[max_key]
    for n in iso_nx.nodes:
        r=255
        g=255*abs((degree_centrality[n]/max_degree)-1)
        b=255*abs((degree_centrality[n]/max_degree)-1)
        rgb = (int(r),int(b),int(g))
        iso_nx.nodes[n]['color']="#"+rgb_to_hex(rgb)

    #nx.write_gexf(iso_nx,"test.gexf")
    iso_net.from_nx(iso_nx)

    for n in iso_net.nodes:
        n['label']=Dicoviz[n['id']]['short']

    #Affichage du réseau
    #Désactiovation dans le doutes mais je ne sais pas si cela affectera le graph pour l'instant.
    iso_net.toggle_physics(True)
    iso_net.show("results/" + outputfile)

    iso_net.set_options("""var options = {
        "nodes": {
            "color": {
            "highlight": {
                "border": "rgba(24,255,22,1)"
            }
            }
        },
        "edges": {
            "color": {
            "highlight": "rgba(255,21,12,1)",
            "inherit": false
            },
            "smooth": {
            "type": "continuous",
            "roundness": 0.5
            }
        },
        "physics": {
            "forceAtlas2Based": {
            "gravitationalConstant": -227,
            "springLength": 100
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based"
        }
    }
    """)

    #iso_net.force_atlas_2based()
    iso_net.show("iso_net.html")

if __name__ == "__main__":
   main(sys.argv[1:])
   
def rgb_to_hex(rgb):
  return '%02x%02x%02x' % rgb