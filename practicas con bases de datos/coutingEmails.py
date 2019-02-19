""" Cuenta el numero de ocurrencias de todas las direcciones
	de email que aparecen en un documento y las almacena en 
	una base de datos
""" 
import sqlite3 as sql

connection = sql.connect('emaildb.sqlite')
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

file = input('Enter file name: ')

if len(file) < 1:
	file = 'mbox.txt'

fh = open(file)


for line in fh:
	# Obtiene solo las lineas que comienzan con "From"
	# separa la linea por espacios y en la pos. 1 del array obtiene el email
	if not line.startswith('From '): continue
	pieces = line.split()
	email = pieces[1]

	# Almacena el email en la tabla
	cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
	row = cur.fetchone()

	# Si ya un email existe, actualiza el contador
	if row is None:
		cur.execute('''INSERT INTO Counts (email, count) VALUES(?,1)''',(email,))
	else:
		cur.execute('UPDATE Counts SET count = count+1 WHERE email = ?',(email,))

# Guarda los cambios en disco una vez sale del ciclo, ( > eficiencia)
connection.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]),row[1])

cur.close()