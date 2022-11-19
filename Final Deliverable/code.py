import numpy as np
import cv2
import os
from keras.models import load_model
from flask import Flask, render_template, Response
import tensorflow as tf
from gtts import gTTS
global graph
global writer
from skimage.transform import resize


graph = tf.compat.v1.get_default_graph()
writer = None

model = load_model('aslpng1.h5')

vals = ['A','B','C','D','E','F','G','H','I']

app = Flask(__name__,template_folder='template')

print("[INFO] accessing video stream.....")
camera= cv2.VideoCapture(0)


pred=""

@app.route('/')
def index():
    return render_template('index.html')


def detect(frame):
    vals = ['A','B','C','D','E','F','G','H','I']
    img = resize(frame,(64,64,1))
    img = np.expand_dims(img,axis=0)
    if(np.max(img) > 1):
        img = img/225.0
    with graph.as_default():
            prediction = model.predict_classes(img)
    print(prediction)
    pred=vals[predication[0]]
    print(pred)
    return pred




@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundry=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)