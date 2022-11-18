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
vs = cv2.VideoCapture(0)


pred=""

@app.route('/')
def index():
    return render_template('index.html')