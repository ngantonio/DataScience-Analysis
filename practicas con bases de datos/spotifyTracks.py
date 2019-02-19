"""
     Toma datos de una playlist de spotify en formato XML
     y busca dentro del XML los datos del artista, del album y 
     de la pista para posteriormente almacenarlos en una DB.
"""
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('multiTracksdb.sqlite')
cur = conn.cursor()

# Creando la base de datos para las pistas...
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


# Nombre del archivo a procesar
fname = 'Library.xml'

# encargada de comprobar si la primera rama del arbol de pistas
# es realmente el ID de la misma
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


# Frafmento del Arbol XML que nos será util para obtener la informacion
# de las pistas:

"""
 <key>Track ID</key><integer>369</integer>
 <key>Name</key><string>Another One Bites The Dust</string>
 <key>Artist</key><string>Queen</string>
"""

# Convertimos el codigo XML en un arbol XML basado en listas
# con Element Tree
stuff = ET.parse(fname)

# Navegamos en profundidad por las 3 etiquetas que existen
# antes de encontrar la primera pista (previo analisis del documento XML)
all = stuff.findall('dict/dict/dict')

# Para cada pista, obtenemos los datos y almacenamos en la DB
for entry in all:

    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    genre = lookup(entry, 'Genre')
    #print(genre)
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None : 
        continue

    print(name, artist, genre, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    #GENRE
  
    cur.execute('''INSERT OR IGNORE INTO Genre(name)
        VALUES( ? )''', (genre,) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ',(genre, )) 
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
         VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

# Guardamos en disco y cerramos la conexion
conn.commit()
cur.close()
