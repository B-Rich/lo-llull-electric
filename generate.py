# coding=UTF-8

from __future__ import print_function
import json
import numpy as np
import random
import sys
import codecs
from keras.models import load_model

# Hack for tensorflow 0.11 and keras incompatibility
# https://github.com/fchollet/keras/issues/3857
import tensorflow as tf
tf.python.control_flow_ops = tf

GEN_LEN = 600
path = "textos/all.txt"
diversity = 0.5
modelname = 'models/gaseta_v0155.h5'
inputseed = u"En el cas del personal provinent d'un organisme autònom o ens instrumental de l'Ajuntament de Barcelona, la seva presa de possessió es durà a terme a partir del primer dia hàbil del mes següent a la publicació de la resolució del concurs a la Gaseta Municipal. En el cas que la publicació s'efectuï en la darrera Gaseta Municipal del mes, la presa de possessió es diferirà al primer dia hàbil del segon mes comptat des de la publicació de l'esmentada Gaseta."
 
text = open(path).read().lower()

chars = sorted(list(set(text)))
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

model = load_model(modelname)
maxlen = model.input_shape[1]

rawtext = inputseed.encode('utf-8')
text = rawtext[-maxlen:].rjust(maxlen)

generated = ''
#start_index = random.randint(0, len(text) - maxlen - 1)
sentence = text #[start_index: start_index + maxlen]
#generated += sentence
for i in range(GEN_LEN):
    x = np.zeros((1, maxlen, len(chars)))
    for t, char in enumerate(sentence):
        if (char in char_indices):
            x[0, t, char_indices[char]] = 1.
    preds = model.predict(x, verbose=0)[0]
    next_index = sample(preds, diversity)
    next_char = indices_char[next_index]
    generated += next_char
    sentence = sentence[1:] + next_char
    sys.stdout.write(next_char)
    sys.stdout.flush()
response={"text": generated}
#print (generated)

