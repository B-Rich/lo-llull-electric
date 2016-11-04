[Version en Castellano abajo] - [Scroll down for english version]

![alt tag](https://pbs.twimg.com/profile_images/788473798290989057/rpTkbBns_400x400.jpg)


## Ramon Llull bot elèctric https://twitter.com/lollullelectric

Per a una introducció general del projecte: http://www.bsc.es/viz/llull/

Dins de l'any Llull, aquest projecte fa servir textos originals de Ramon Llull per l'entrenament d'una Xarxa Neuronal Recurrent (RNN) que es fa servir per generar twits de manera automàtica. El procés es realitza de manera totalment no supervisada. Fem servir una Long-Short Term Memory (LSTM) per a la capa RNN, trobareu una bona introducció a les LSTM [aquí](http://colah.github.io/posts/2015-08-Understanding-LSTMs/).

Hem inclòs una carpeta amb alguns textos de Ramon Llull per fer l'entrenament de la RNN. Canviant únicament el material d'entrenament la xarxa aprèn l'estil d'un altre autor. Podeu provar-ho fent servir el text d'unes 200 cançons de Bob Dylan que també hem afegit.


### Instal·lació

Descarregar el ZIP de gihub, o fer 

```bash
$ git clone https://github.com/arturgs/lo-llull-electric.git
```

#### Dependències:

Per poder executar el projecte necessitareu també tenir instal·lats

[Keras](https://keras.io) : Llibreria d'alt nivell per gestionar la RNN.

[Theano](http://deeplearning.net/software/theano/) o [Tensorflow](https://www.tensorflow.org/) : Llibreries de baix nivell utilitzades per Keras, només cal tenir instal·lada una de les dues (Recomanable: disposar d'una GPU i instal·lar les version per GPU d'aquestes llibreries).

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

### A la premsa

+ [Un robot que escriu com Dylan, a ElPeriodico.cat (4-11-2016)](http://www.elperiodico.cat/ca/noticias/societat/robot-que-escriu-com-dylan-5606011)
+ [Que una inteligencia artificial opine por ti, a TIU mag (27-10-2016)](http://www.tiumag.com/features/interviews/lo-llull-electric-entrevista-barcelona-supercomputing-centre/)

---

---

￼![alt tag](https://pbs.twimg.com/profile_images/788473798290989057/rpTkbBns_400x400.jpg)

## Ramon Llull bot electrico https://twitter.com/lollullelectric

Para una introducción general del proyecto: http://www.bsc.es/viz/llull/index_es.html

Dentro del año Llull, este proyecto utiliza textos originales de Ramon Llull para el entrenamiento de una Red Neuronal Recurrente (RNN) que se utiliza para la generación automática de tweets. El proceso se realiza de manera totalmente no supervisada. Utilizamos una Long-Short Term Memory (LSTM) para la capa RNN, encontraréis una buena introducción a las LSTM 
[aquí](http://colah.github.io/posts/2015-08-Understanding-LSTMs/).

Hemos incluido una carpeta con algunos textos de Ramon Llull para realizar el entrenamiento de la RNN. Cambiando únicamente el material de entreno, la Red aprende el estilo de otro autor. Podéis probarlo utilizando el texto de unas 200 canciones de Bob Dylan que también incluimos en el proyecto.

### Instalación

Descargar el ZIP de gihub, o  

```bash
$ git clone https://github.com/arturgs/lo-llull-electric.git
```

#### Dependencias:

Para poder ejecutar el proyecto necesitaréis tener instalados:

[Keras](https://keras.io) : Librería de alto nivel para gestionar la RNN.

[Theano](http://deeplearning.net/software/theano/) o [Tensorflow](https://www.tensorflow.org/) : Librerías de bajo nivel utilizadas por Keras, solo necesitáis tener instalada una de las dos (Recomendable: disponer de una GPU e instalar la versión para GPU de estas librerias).

[Tweepy](http://docs.tweepy.org/en/v3.5.0/install.html?highlight=install) : Gestiona la API de Twitter

(Cualquier otra dependencia se instala automaticamente utilizando `pip` o Anaconda para la instalación de paquetes.)

### Ejecución

[NOTA: necesitaréis crear vuestra propia cuenta de Twitter para utilizar todo el proyecto.]

Para ejecutar el entrenamiento de la RNN 
```bash
$ train_llull.py
```
Esta es la parte más costosa computacionalmente de todo el proyecto. 
El proceso de entrenamiento genera un conjunto de RNN, progresivamente con menos error. Estas RNNs se utilizan para generar tweets, ejecutando

```bash
$ tweet.sh
```
### Otros recursos
+ [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
+ [Adventures in Narrated Reality, Part II](https://medium.com/artists-and-machine-intelligence/adventures-in-narrated-reality-part-ii-dc585af054cb#.mzbo3mtdf)

### En prensa
+ [Un robot que escribe como Dylan, en ElPeriodico.cat (4-11-2016)](http://www.elperiodico.com/es/noticias/societat/robot-que-escriu-com-dylan-5606011)
+ [Que una inteligencia artificial opine por ti, a TIU mag (27-10-2016)](http://www.tiumag.com/features/interviews/lo-llull-electric-entrevista-barcelona-supercomputing-centre/)


---
---

![alt tag](https://pbs.twimg.com/profile_images/788473798290989057/rpTkbBns_400x400.jpg)
## Ramon Llull electric bot https://twitter.com/lollullelectric

Inside the celebrations of the aniversary of Ramon Llull, this project takes his original texts to train a Recurrent Neural Network (RNN) used to automatically generate tweets. This proces is totally unsupervised. We use a Long-Short Term Memory (LSTM) for the RNN layer, you'll find an excellent introduction to LSTMs [here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/).

We have included some texts by Ramon Llull for the RNN training. Change only the training material, and the NN will learn any other author's style. You can try this yourself with more than 200 songs by Bob Dylan included also in the project's folder.

### Instalation

Just download the ZIP from gihub, or  
```bash
$ git clone https://github.com/arturgs/lo-llull-electric.git
```

#### Dependencies:

You will need to install these libraries

[Keras](https://keras.io) : Top level library for managing RNN.

[Theano](http://deeplearning.net/software/theano/) o [Tensorflow](https://www.tensorflow.org/) : Low level NN libraries used by Keras. You only need one of these two. (Recommended: use a GPU and install the corresponding GPU versions of these libraries.)

[Tweepy](http://docs.tweepy.org/en/v3.5.0/install.html?highlight=install) : Manager for Twitter's API

(Any other dependencies should be automatically installed by `pip` or Anaconda.)

### Execution

[NOTE: you'll need your own Twitter account to run the full project.]

To start the training proces of the RNN 
```bash
$ train_llull.py
```
This is by far the most computationally-demanding part of the project.
The training process will generate a set of RNN, progressively more accurate. These RNNs are used to write tweets, running
```bash
$ tweet.sh
```

### Other resources
+ [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
+ [Adventures in Narrated Reality, Part II](https://medium.com/artists-and-machine-intelligence/adventures-in-narrated-reality-part-ii-dc585af054cb#.mzbo3mtdf)

### On the press
+ [Un robot que escribe como Dylan, at ElPeriodico.cat (4-11-2016)](http://www.elperiodico.com/es/noticias/societat/robot-que-escriu-com-dylan-5606011)
+ [Que una inteligencia artificial opine por ti, at TIU mag (27-10-2016)](http://www.tiumag.com/features/interviews/lo-llull-electric-entrevista-barcelona-supercomputing-centre/)
