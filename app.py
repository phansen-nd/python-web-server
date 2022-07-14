from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import subprocess

app = Flask(__name__)
app.isPlaying = False
app.proc = None

@app.route('/')
def index():
    return 'Hello, world'

@app.route('/audio', methods=['POST'])
def get_audio_url():
    print("Got URL request to /audio")
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        download_and_play(json['url'])
        return json
    else:
        return 'Content-type not supported'

def download_and_play(url):
    print("Playing from URL: %s" % url)
    filename = 'audio.m4a'
    doc = requests.get(url)
    if (app.isPlaying): return
    app.isPlaying = True
    with open(filename, 'wb') as f:
        f.write(doc.content)

    app.proc = subprocess.call(['vlc', filename])

@app.route('/audio/pause', methods=['GET'])
def pause():
    print("Got pause POST")
    app.isPlaying = False
    app.proc.kill()
    
if __name__ == '__main__':
    isPlaying = False
    app.run(debug=True, host='0.0.0.0')
