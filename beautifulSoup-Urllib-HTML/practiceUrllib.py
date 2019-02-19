#descargar beautifulsoup
#https://pypi.python.org/pypi/beautifulsoup4

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#para ignorar los errores de certificado ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#pedimos al usuario una url
url = input('Enter : ')
html = urllib.request.urlopen(url, context=ctx).read()

#estamos dando un HTML feo y desagradable que no tendría ningún sentido en absoluto. 
#Por favor léalo y quite todas las cosas raras, descúbralo y devuélvanos un objeto. 

# Pero este objeto de sopa está limpio. Y entonces, lo que podemos hacer es que podemos recuperar 
#cualquier tag html de alli.
soup = BeautifulSoup(html,'html.parser')

#Así que podemos hablar con este objeto y decir, pregúntalo, dame todas las etiquetas a. 
#y con get obtenemos los atributos que están en la etiqueta. 

#obtenemos una lista de todos los tags a

tags = soup('a')
for tag in tags:
	print(tag.get('href',None))



#Vamos a recuperar todo el HTML. Vamos a hacer una URL abierta como lo hicimos antes. 
#Ahora esto nos devolvería algo que podríamos recorrer línea por línea con un bucle for. 
#Pero en cambio, vamos a decir, oigan todo el asunto. Y eso básicamente nos devuelve todo el
#documento en esa página web. En una sola cadena grande con nuevas líneas al final de cada línea.

#Y esto no está en Unicode pero es probable que sea una cadena UTF-8. 
#Pero resulta que BeautifulSoup sabe cómo tratar con UTF-8
#y También sabe cómo tratar con cadenas de Unicode.


#************************************************************

#con respecto al ssl:

# Ahora, el SSL es si está mirando una página que tiene SSL. a
#así que voy a ir a https://www.si.umich.edu, y obtendrá un montón de enlaces.

# Y si no fuera por el codigo de SSL, este HTTPS no hubiera funcionado. 
#Y, no es que ese sitio web tuviera una URL mala, tiene un certificado que no está en la lista oficial de Python.

