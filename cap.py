import requests
import os
from flask import Flask
from flask import render_template
from flask import request
from captionbot import CaptionBot
from flask_bootstrap import Bootstrap
from werkzeug import secure_filename
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tensorflow as tf
from collections import defaultdict
from flask_gtts import gtts
from gtts import gTTS
from playsound import playsound
from io import StringIO
from PIL import Image
sys.path.append("..")
from utils import label_map_util
from utils import visualization_utils as vis_util


language = 'en'
c=CaptionBot()

app = Flask(__name__)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = os.path.basename('/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
  file = request.files['file']

  f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
  file.save(f)
  print(f)
  image_caption = c.file_caption(f) 
  return render_template('index.html', image_caption=image_caption)
    
@app.route("/success", methods = ['POST','GET'])
def success():
    text = c.file_caption(f)
    tts = gTTS(text=text, lang='en')
    return render_template("success.html",value = text)
    tts.save("text.mp3")

if __name__ == '__main__':
  app.run(debug=True, port=3000)
