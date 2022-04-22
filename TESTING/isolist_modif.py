import re
import jsonreading_modif
import json

ISOList = jsonreading_modif.readJsonFileInit("isolist.json")

for key in ISOList.keys():
    ISOList[key]["lien"] = re.sub("fr/","",ISOList[key]["lien"])

with open('isolist.json', 'w') as fp:
    json.dump(ISOList, fp, sort_keys=True, indent=4, ensure_ascii=False)