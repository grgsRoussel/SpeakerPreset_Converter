import numpy as np
import sofar as sf
import pyfar

class spkdata:
    def __init__(self):
        self.data = sf.Sofa("AnnotatedEmitterAudio", True)
        # delete default emiter position
        pass

    def json2sofa(self):
        self.data
        pass

    def xmlGris2sofa(self, xmlGris):

        nb_spk = len(xmlGris.SPEAKER_SETUP)
        self.data.EmitterPosition = np.zeros([nb_spk,3])

        for idx in range(nb_spk):
            self.data.EmitterPosition[idx] = np.array([0,0,idx])


        a = 0

        pass