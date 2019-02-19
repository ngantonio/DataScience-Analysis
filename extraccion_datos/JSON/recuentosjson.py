#El programa solicitará una URL, leerá los datos JSON de esa URL usando urllib 
#y luego analizará y extraerá los recuentos de comentarios de los datos JSON, calculará la suma de los números en el archivo.
#URL de muestra: http://py4e-data.dr-chuck.net/comments_145683.json

import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving ', url)

data = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved ', len(data), ' characters')

#solo almacenamos la lista de comentarios
info = json.loads(data)
info = info['comments']

#Imprimimos el JSON con un poco de formato:
print(json.dumps(info, indent=4))

#extraemos el count de cada uno de los cometarios
#y calculamos su suma
sum = 0
for obj in info:

   number = int(obj['count'])
   sum += number
print('Sum: ',sum)