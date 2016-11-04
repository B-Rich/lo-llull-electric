#encoding=utf-8

from __future__ import print_function
import json
import numpy as np
import random
import sys
from keras.models import load_model
import time
from flask import Flask,jsonify,render_template,request,make_response,url_for
# Hack for tensorflow 0.11 and keras incompatibility
# https://github.com/fchollet/keras/issues/3857
import tensorflow as tf
tf.python.control_flow_ops = tf


################################################################
################    NN stuff
################################################################
path = "../textosLlull/cleaner.txt"
text = open(path).read().lower()
#print('corpus length:', len(text))

chars = sorted(list(set(text)))
#print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

model = load_model('../models/clean_SINGLELAYER1228.h5')
maxlen = model.input_shape[1]

temperatures = [ 0.5, 0.7, 0.9]

def calcular(texto,diversity,generateLength=10):
    #print (type(pregunta))
    pregunta = texto.encode('utf-8')
    text = pregunta[-maxlen:].rjust(50).lower()
    generated = ''
    sentence = text
    probabilities = {}
    for i in range(generateLength):
        x = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            if (char in char_indices):
                x[0, t, char_indices[char]] = 1.
        preds = model.predict(x, verbose=0)[0]
        probabilities[i] = [ float(num) for num in preds ]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]
        generated += next_char
        sentence = sentence[1:] + next_char
    #print (generated)
    str_response=  json.dumps({"text": generated, "probabilities": probabilities})
    response=make_response(str_response)
    response.mimetype='application/json;charset=utf-8'
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

################################################################
################    Web server stuff
################################################################

APP = Flask(__name__)
APP.debug = False

@APP.route("/indices/")
def indices():
    ci = dict((c.decode('macroman'), i) for i, c in enumerate(chars))
    ic = dict((i, c.decode('macroman').encode('utf-8')) for i, c in enumerate(chars))
    return jsonify(char_indices= ci,indices_char = ic)

@APP.route("/ramon/" )
def contestar():
    temperature=float(request.args.get("diversity", "70"))/100.0
    chars=int(request.args.get("chars", "10"))
    text = request.args.get("text","")
    respuesta = calcular(text,temperature,chars)
    #respuesta = calcular()
    return respuesta #jsonify(a)

@APP.route("/" )
def main():
    print (url_for("static",filename="realtime.js"))
    return render_template("index.html")

if (__name__=="__main__"):
    APP.run()
