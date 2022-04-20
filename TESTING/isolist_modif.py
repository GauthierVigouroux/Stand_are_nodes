import re
import jsonreading_modif
import json

ISOList = jsonreading_modif.readJsonFileInit("isolist.json")

for key in ISOList.keys():
    ISOList[key]["lien"] = re.sub("ed-1:|ed-2:|ed-4:|ed-5:|v1:|v2:|v3:|v4:","",ISOList[key]["lien"])

with open('isolist.json', 'w') as fp:
    json.dump(ISOList, fp, sort_keys=True, indent=4, ensure_ascii=False)