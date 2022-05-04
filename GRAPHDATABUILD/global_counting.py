def global_count_citation (ISODict):
    for i in ISODict.keys():
        for j in ISODict.keys():
            ISODict[i]["global_count_citation"] += ISODict[j]["dependance"].count(i)
        