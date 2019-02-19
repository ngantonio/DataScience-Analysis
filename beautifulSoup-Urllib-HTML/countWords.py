# Cuenta el numero de palabras unicas en un texto HTML

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#contaremos las palabras que mas apaceren...
counts = dict()
for line in fhand:
	#no saltos de linea
	line = line.decode().strip()
	#separamos por espacios
	words = line.split()

	for word in words:
		counts[word]= counts.get(word,0)+1

print(counts)
	