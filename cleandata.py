import json
import jsonreading

ISODict = jsonreading.readJsonFileInit("data.json")

for key in ISODict.keys():
    link = ISODict[key]["lien"]
    link = link.split(":clause")
    link = link[0]
    ISODict[key]["lien"] = link

with open('data_modif.json', 'w') as fp:
    json.dump(ISODict, fp, sort_keys=True, indent=4, ensure_ascii=False)