"""
	Cuenta todas las etiquetas "span" dentro de un codigo html
	Data de prueba: http://py4e-data.dr-chuck.net/comments_145680.html
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

content = list()
tags = soup('span')
for tag in tags:
	content.append(int(tag.contents[0]))

print(sum(content))