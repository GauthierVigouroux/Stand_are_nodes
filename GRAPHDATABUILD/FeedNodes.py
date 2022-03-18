import code
from optparse import Values
from os import link
from neomodel import (StructuredNode, UniqueIdProperty, StringProperty, DateProperty, config, RelationshipFrom, RelationshipTo)

class Norme(StructuredNode):
    uid = UniqueIdProperty()
    code = StringProperty(unique_index=True)
    titre = StringProperty(unique_index=True)
    link = StringProperty()
    dependencies = RelationshipTo('Norme','DEPENDS OF')

class interact_db:

    def __init__(self, uri, user, password):
        config.DATABASE_URL = f'bolt://{user}:{password}@{uri}'
    
    def init_db_nodes(ISODict):
        for key,values in ISODict:
            norme_nodes = Norme(
                code = ISODict[key].keys(),
                titre = values[0],
                link = values[1]
            ).save() # Je suis pas sur de ce coup là
