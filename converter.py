import importer
import exporter
import spkdata

import numpy as np

class Convert:

    def __init__(self):
        spkDataIn = []
        spkDataOut = []
        self.spk = spkdata.spkdata()

    def spatgris2sparta(self):
        print("Converting Spatgris format to Sparta / IEM format")
        self.spkDataIn = importer.spatgris()
        self.spk.xmlGris2sofa(self.spkDataIn)
        exporter.sparta()


    def sparta2spatgris(self):
        print("Converting Sparta / IEM format format to Spatgris")
        self.spkDataIn = importer.sparta()
        self.spk.json2sofa()
        exporter.spatgris()

