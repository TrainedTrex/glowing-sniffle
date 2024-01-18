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

        self.spotifyKey = config["spotifyKey"]
        self.adminKey = config["adminKey"]
        self.useConfig = True
        
        f.close()

    def _auth(self):

        # Auth workflow for getting information from Spotify
        
        return

    def getCurrentSong(self):
        
        musicJSON = {"MusicInfo":self.song}
        JSONstring = json.dumps(musicJSON)

        return JSONstring
    
    def getSongDuration(self):

        return

    def getCurrentLocation(self):

        return
    
    def offline(self):

        #workflow to return json when user is offline.

        return
    
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
    
        