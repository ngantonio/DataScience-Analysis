
"""
	Extrae los valores de los links href de un archivo de links recursivos de una posicion
	en particular contando desde el primer links, un numero "count" de veces, debe imprimir
	el apellido que se encuentre en esa posicion

	#URL TEST: http://py4e-data.dr-chuck.net/known_by_Niteesha.html
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter Count: '))+1
pos = int(input('Enter Position: '))

for i in range(count):
	
	print('Retrieving: ', url)
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	url= tags[pos-1].get('href',None)