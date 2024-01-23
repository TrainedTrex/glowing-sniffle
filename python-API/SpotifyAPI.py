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

        #Get the current time into the song, TBD on if this is going to be used. 

        return
    
    def offline(self):
        
        #workflow to return json when user is offline.
        isOffline = bool

        return isOffline
    
        