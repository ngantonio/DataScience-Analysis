#Funciones creadas para la manipulacion de la API de twitter
from tweepy import StreamListener

#creamos la clase escuchadora*

class FiniteStreamListener(StreamListener):
    
    #la funcion que obtendra los tweets

    def __init__(self, number_of_tweets):
        self.number_of_tweets = number_of_tweets	#Inicializamos un atributo con el numero de tweets enviado como parametro
        self.tweets = []	#iniciamos una lista vacia que contendra nuestros tweets
        super().__init__()	#carga el constructor padre
        
    #este metodo se debe definir de forma obligatoria, y define la operacion logica 
    #que se debe cumplir cada vez que la api obtenga una nuevo tweet, en este caso, que la lista  de tweets sea < a 100
    def on_status(self, status):
    	#si la lista de tweets es < al parametro de numero de tweets
        if len(self.tweets) < self.number_of_tweets:
        	#se agrega ese tweet a la lista
            self.tweets.append(status.text)
        else:
            return False
