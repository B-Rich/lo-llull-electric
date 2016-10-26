'''Modified example script from Keras lstm char generator.
https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py

Saves the network every some iterations (one epoch per iteration)

Notice the two different datasets, one is cleaner but much smaller

Output is 140 chars long (yes, for Twitter)

Architecture now is similar to Torch-rnn example
'''
from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import re



def put_space(text):
	sentence = ''
	for word in text:
		sentence += word+' '
	return sentence


MAX_ITERATIONS = 1000
SAVE_NN_EVERY_ITERATIONS = 10
MODEL =  "clean" # "long"
BATCH_SIZE = 20
LSTM_SIZE = 300


if MODEL=="clean":
    path = "textosLlull/cleaner.txt"
else:
    path = 'textosLlull/all.txt'
    
text = open(path).read().lower()
text = re.sub(r'[^\w\s]','',text) # remove punctuation, recover it somewhere
text = text.split()


words = set(text)
print('total words:', len(words))

word_indices = dict((w, i) for i, w in enumerate(words))
indices_word = dict((i, w) for i, w in enumerate(words))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 15
step = 5
sentences = []
next_word = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_word.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(words)), dtype=np.bool)
y = np.zeros((len(sentences), len(words)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, wd in enumerate(sentence):
        X[i, t, word_indices[wd]] = 1
    y[i, word_indices[next_word[i]]] = 1


# build the model: a single LSTM
print('Build model...')
model = Sequential()
model.add(LSTM(LSTM_SIZE, return_sequences=True, input_shape=(maxlen, len(words))))
model.add(Dropout(0.2))
model.add(LSTM(LSTM_SIZE))
model.add(Dropout(0.2))
model.add(Dense(len(words)))
model.add(Activation('softmax'))

#optimizer = RMSprop(lr=0.01, clipnorm=5.,  decay=0.0002) # 'decay' nor working in THEANO
optimizer = RMSprop(lr=0.01, clipnorm=5.)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# train the model, output generated text after each iteration
for iteration in range(1, MAX_ITERATIONS):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    model.fit(X, y, batch_size=BATCH_SIZE, nb_epoch=1)

    if iteration%SAVE_NN_EVERY_ITERATIONS==0:
        print ("Saving model...")
        outpath="models/"+MODEL+"_"+str(iteration)+".h5"
        model.save(outpath)
        
    start_index = random.randint(0, len(text) - maxlen - 1)

    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('----- diversity:', diversity)

        generated = ''
        sentence = put_space(text[start_index: start_index + maxlen])
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sentence = sentence.split()

        for i in range(140):
            x = np.zeros((1, maxlen, len(words)))
            for t, wd in enumerate(sentence):
                x[0, t, word_indices[wd]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_word = indices_word[next_index]

            generated += next_word+" "
            sentence = sentence[1:] + [next_word]

        print('generated============='+generated)

