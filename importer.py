import json 
import numpy as np
import untangle as xml

def sparta():
    print("Sparta / IEM importer")

    with open("./SpartaJSONExemple.json",'r') as file:
        return json.load(file)

def spatgris():
    print("SpatGris importer")
    xmldata = xml.parse("./Dome93(32-32-16-8-4-1)Subs5 Satosphere.xml")
    return xmldata

def iem():
# This function is exactly the same as sparta for now
    sparta()

def sofa():
    pass
