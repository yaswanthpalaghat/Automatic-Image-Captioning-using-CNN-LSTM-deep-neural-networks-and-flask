import soco, time

from gtts import gTTS
from mutagen.mp3 import MP3
from captionbot import CaptionBot
from soco.snapshot import Snapshot
from flask import Flask, request, render_template, redirect

language = 'en'
c=CaptionBot()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])

class Sonos():
    def play(self, text):
	    file = request.files['file']
	    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
	    file.save(f)
	    print(f)
	    text = c.file_caption(f)
	    tts = gTTS(text=text, lang='en')
	    tts.save("sound.mp3")
	    audio = MP3("sound.mp3")
		
		# print soco.discover()
		# for speaker in soco.discover(timeout=5):
		# 	print speaker
			# snap = Snapshot(speaker) 
			# snap.snapshot()

			# speaker.volume = 50
			# speaker.play_uri("http://192.168.0.3:8080/sound.mp3")

			# time.sleep(audio.info.length)
			# snap.restore()

if __name__ == '__main__':
	app.run(debug=True, port=2000)
	