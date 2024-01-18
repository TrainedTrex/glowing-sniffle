from asyncore import read
import glob
import json
import re
import sys
import os

class SpotifyAPI:

    def __init__(self):
        self.configFile = ''
        self.poiFile = ''
        self.useConfig = True
        self.outputFile = ''


    def _readConfig(self): 
        f = open('./config.json')
        config = json.load(f)

        #self.tleFile = config["tleFile"]
        self.useConfig = False
        #self.licenseFile = config["licenseFile"]
        
        f.close()

    def getCurrentSong(self):
        
        songJSON = {"SatelliteList":self.song}
        JSONstring = json.dumps(songJSON)

        return JSONstring

    def propagate(self):
        
        return
    
    def generateCZML(self, interval):
        
        name = "TLE_Propagation"
        description = "CZML document containing propagated TLE data from all of the satellites contained in the input file."
        prettyFormatting = True
        requestedInterval = interval
        #print(interval)
        #print(interval.Start)
        clock = Clock()
        clock.Interval = interval 
        clock.CurrentTime = interval.Start
        
        CzmlDoc = CzmlDocument()
        CzmlDoc.Name = name
        CzmlDoc.Description = description
        CzmlDoc.PrettyFormatting = prettyFormatting
        CzmlDoc.RequestedInterval = requestedInterval
        CzmlDoc.Clock = clock
    
        print("Done generating the CZML Document")
        return CzmlDoc
        
    def getKeys(self):

        return
    
    def getOrbitRegime(self,TLE):
    
        ecc = TLE.Eccentricity
        meanMotion = TLE.MeanMotion
        
        a = pow((8681663.653 / meanMotion),(2 / 3))
        
        hp = a * (1 - ecc) - 6371
        ha = a * (1 + ecc) - 6371
        
        if (ha < 2000):
            orbitType = 'LEO'
        elif (hp > (40164 - 6371) and ha < (44164 - 6371)):
            orbitType = 'GEO'
        elif (hp > 2000 and ha < (40164 - 6371)):
            orbitType = 'MEO'
        elif (hp < 2000 and ha > (40164 - 6371)):
            orbitType = 'GTO'
        else:
            orbitType = 'HEO'
            
        return orbitType
    
        