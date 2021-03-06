'''
'''

from __future__ import print_function
import json
import numpy as np
import random
import sys
import codecs
from keras.models import load_model
import util_twitter
import time

minutesBetweenTweets = 20

path = "textosLlull/cleaner.txt" 
text = open(path).read().lower()
print('corpus length:', len(text))

chars = sorted(list(set(text)))
print('total chars:', len(chars))
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

def cleanText(original): #Remove @usernames and http links
    splitted = original.strip().split(" ")
    together = []
    for word in splitted:
        if (word.find("@")<0 and word.find("http")<0):
            together.append(word)
    return " ".join(together)

model = load_model('models/clean_655.h5')
maxlen = model.input_shape[1]

done = {}
logger=open("alreadyDone.txt",'r+',0)
for line in logger:
    sline = line.strip().split()
    done[sline[0]]=sline[1]

hashtag = ""

temperatures = [0.2, 0.4, 0.7, 1.0]
try:
 while True:
   following = []
   fi=open('following.txt','r')
   for line in fi:
      following.append(line.strip())
   fi.close()
   fi=open("configuration.txt",'r')
   for line in fi:
      sline=line.strip().split()
      if (sline[0]=="minutesBetweenTweets"):
         minutesBetweenTweets = sline[1]
      elif (sline[0]=="model"):
         model = load_model(sline[1])
         maxlen = model.input_shape[1]
      elif (sline[0]=="hashtag"):
         hashtag = sline[1]
   fi.close()
   # Future: util_twitter.get_following("lollullelectric")
   #for user in following:
   user = np.random.choice(following)
   print ("Going to answer to "+user)
   try: 
     tweets = util_twitter.get_twits(user)
     tweet = np.random.choice(tweets)
     #for tweet in tweets:
     rawtext = tweet.text.encode('utf-8')
     text = cleanText(rawtext)
     if len(text)<=maxlen:
        print ("Too short: "+text)
     elif (tweet.id in done):
        print ("Tweet already quoted")
     else:
      try:
        diversity = np.random.choice(temperatures)
        generated = ''
        start_index = random.randint(0, len(text) - maxlen - 1)
        sentence = text[start_index: start_index + maxlen]
        #generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(115-len(hashtag)):
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
        generated += " "+hashtag+" https://twitter.com/"+(user[1:])+"/status/"+str(tweet.id)
        response=util_twitter.twit_text(generated)
        done[tweet.id]=response.id
        logger.write(str(tweet.id)+","+str(response.id)+"\n")
        time.sleep(minutesBetweenTweets*60)
        print("\n")
      except:
        print ("Had problems with "+rawtext)
        continue
   except:
      print (user+" has blocked us")
except KeyboardInterrupt:
 logger.close()
 print ("Interrupted")
