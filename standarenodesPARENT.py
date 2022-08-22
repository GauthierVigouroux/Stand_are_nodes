import jsonreading
import PARSE_HTML.parse_html
import json
from GRAPHDATABUILD.global_counting import global_count_citation
import sys, getopt

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
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    #Récupération du dico original
    ISODict = jsonreading.readJsonFileInit(inputfile)
    ISODictAntiCircular = list(ISODict)
    #Récupération des infos sur le site de l'ISO afin de compléter les tuples des différents liens
    #.items() retourne un tuple donc hashable
    for standardlink in ISODictAntiCircular:
        print(ISODict[standardlink]["short"])
        ISODict = PARSE_HTML.parse_html.isorequests(standardlink,ISODict)
        #print(list(ISODict.items())[-1]) #Permet de voir l'évolution de la taille du dico
        # print(ISODict[standard])
    ISODict = global_count_citation(ISODict)
    #print(ISODict)
    with open(outputfile, 'w') as fp:
        json.dump(ISODict, fp, sort_keys=True, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1:])