#En esta tarea, escribirás un programa Python algo similar a https://py4e.com/code3/geoxml.py .
#El programa solicitará una URL, leerá los datos XML de esa URL usando urllib y 
#luego analizará y extraerá los recuentos de comentarios de los datos XML, 
#calculará la suma de los números en el archivo e ingresará la suma

#URL de ejemplo: http://py4e-data.dr-chuck.net/comments_145682.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving ', url)

data = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved ', len(data), ' characters')

comment_info = ET.fromstring(data)

counts = comment_info.findall('comments/comment/count')
print('Count ', len(counts))

sum = 0
for number in counts:
   number = int(number.text)
   sum += number
print('Sum: ',sum)
