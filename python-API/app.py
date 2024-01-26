from flask import Flask
from flask_cors import CORS
from SpotifyAPI import getCurrentSong

app = Flask(__name__)
CORS(app)

@app.route('/api')
def Home():
    return 'This is the homepage for the API'

@app.route('/api/CurrentSong')
def Song():
    curSong = getCurrentSong()
    return curSong

@app.route('/api/Art')
def albumnArt():
    return 

if __name__ == '__main__':
    app.run(debug=True)