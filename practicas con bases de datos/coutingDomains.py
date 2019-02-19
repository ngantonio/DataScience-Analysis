""" cuenta el número total de dominios de emails
	y los almacena en una base de datos
"""
import sqlite3 as sql

# Iniciamos las variables de conexión, y creamos la base de datos.
connection = sql.connect('domaindb.sqlite')
cur = connection.cursor()

# Verificamos si la tabla existe, si no, la creamos.
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file = input('Enter file name: ')

if len(file) < 1:
	file = 'mbox.txt'

fh = open(file)

# Por cada linea...
for line in fh:

	# Obtenemos solo las lineas que comiencen por "From: "
	if not line.startswith('From: '): continue
	pieces = line.split()

	# Obtenemos el email
	email = pieces[1]

	# Para obtener el dominio del email, separamos el string por el caracter '@'
	# para: marquard@uct.ac.za el dominio se encuentra en la pos. 1
	email = email.split('@')
	domain = email[1]

	# Almacenamos el dominio y Preguntamos si ya existe en la DB, 
	# si es asi, actualiza el contador
	cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
	row = cur.fetchone()

	if row is None:
		cur.execute('INSERT INTO Counts (org, count) VALUES(?,1)',(domain,))
	else:
		cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?',(domain,))

connection.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]),row[1])

cur.close()