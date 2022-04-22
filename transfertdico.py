import json
from pdb import line_prefix
import jsonreading

ISODictv1 = jsonreading.readJsonFileInit("isolist.json")
ISODictv2 = dict()

for key in ISODictv1:
    ISODictv2[ISODictv1[key]["lien"]]={
        "short":key,
        "nom":ISODictv1[key]["nom"]
    }

with open('isolist_v3.json', 'w') as fp:
    json.dump(ISODictv2, fp, sort_keys=True, indent=4, ensure_ascii=False)