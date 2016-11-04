[Version en Castellano abajo] - [Scroll down for english version]

![alt tag](https://pbs.twimg.com/profile_images/788473798290989057/rpTkbBns_400x400.jpg)


## Ramon Llull bot elèctric https://twitter.com/lollullelectric

Per a una introducció general del projecte: http://www.bsc.es/viz/llull/

Dins de l'any Llull, aquest projecte fa servir textos originals de Ramon Llull per l'entrenament d'una Xarxa Neuronal Recurrent (RNN) que es fa servir per generar twits de manera automàtica. El procés es realitza de manera totalment no supervisada.


### Instal·lació

Descarregar el ZIP de gihub o fer 

```bash
git clone https://github.com/arturgs/lo-llull-electric.git
```

#### Dependències:

Per poder executar el projecte necessitareu també tenir instal·lats

[Keras](https://keras.io) : Llibreria d'alt nivell per gestionar la RNN.

[Theano](http://deeplearning.net/software/theano/) o [tensorflow](https://www.tensorflow.org/) : Llibreries de baix nivell utilitzades per Keras, només cal tenir instal·lada una de les dues (Recomanable: disposar d'una GPU i instal·lar les version per GPU d'aquestes llibreries).

[Tweepy](http://docs.tweepy.org/en/v3.5.0/install.html?highlight=install) : Gestiona l'API de Twitter

(Altres dependències s'instal·len automàticament fent servir `pip` o Anaconda per a la instal·lació de paquets.)

### Execució

[NOTA: haureu de crear el vostre compte de Twitter propi per fer servir tot el projecte.]

Per executar l'entrenament de la RNN feu 
```bash
$ train_llull.py
```
Aquesta és la part més costosa computacionalment del projecte.
El procés d'entrenament genera un conjunt de RNN, progresivament amb menys error. Aquestes RNN es fan servir a l'hora de generar els tweets, executant

```bash
$ tweet.sh
```

### Altres recursos

+ [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
+ [Adventures in Narrated Reality, Part II](https://medium.com/artists-and-machine-intelligence/adventures-in-narrated-reality-part-ii-dc585af054cb#.mzbo3mtdf)
+ [Un robot que escriu com Dylan, a ElPeriodico.cat (4-11-2016)](http://www.elperiodico.cat/ca/noticias/societat/robot-que-escriu-com-dylan-5606011)







