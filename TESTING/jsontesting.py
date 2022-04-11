from cgi import test
import imp


import json

dico = {"ISO 19101-1:2014":[
        "ISO 19101-1:2014 Geographic information — Reference model — Part 1: Fundamentals",
        "https://www.iso.org/obp/ui/#iso:std:iso:19101:-1:ed-1:v1:en"
    ],
    "ISO 19101-2:2018":[
        "ISO 19101-2:2018 Information géographique — Modèle de réference — Partie 2: Imagerie",
        "https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:en"
    ]
}

with open('data.json', 'w') as fp:
    json.dump(dico, fp, sort_keys=True, indent=4)