#!/usr/bin/env python
# -*- coding: utf-8 -*-

 
import MySQLdb
import exceptions

 
class myMysql(object):

	def __init__(self):

	# Variable que determina si estamos conectados a MySQL...
		self.connected=0
		self.error=""

	"""
			Realiza la conexion con la base de datos
			Tiene que recibir:
				- host
				- user
				- pw => password
				- database => database name
			Puede recibir:
				- port
			Devuelve True o False
		"""
 
	def mysqlConnect(self,host,user,pw,database,port=3306):

		try:
			self.db = MySQLdb.connect(user=user, passwd=pw, host=host, db=database, port=port, charset="utf8", init_command="set names utf8")
			self.cursor = self.db.cursor()
			self.connected=1
			return True
		except Exception,e:
			self.error="Error: %s" % (e)
		except:
			self.error="Error desconocido"

		return False

		"""
			Funcion que ejecuta una instruccion mysql
			Tiene que recibir:
				- query

			Puede recibir:
				- params => tupla con las variables
				- execute => devuelve los registros
			Devuelve False en caso de error
		"""

	def prepare(self,query,params=None,execute=True):

		if self.connected:
			self.error=""

			try:
				self.cursor.execute(query,params)
				self.db.commit()

				if execute:

					# convert de result to dictionary
					result = []
					columns = tuple([d[0].decode('utf8') for d in self.cursor.description])

					for row in self.cursor:
						result.append(dict(zip(columns, row)))
					return result

				return True

			except Exception,e:
				self.error="Error: %s" % (e)
		return False

 	
		"""
			Funcion que devuelve el ultimo id añadido
		"""

	def lastId(self):
		return self.cursor.lastrowid

 
	def affectedRows(self):
		return self.cursor.rowcount

		
		"""
			Funcion para cerrar la conexion con la base de datos
		"""
	def mysqlClose(self):

		self.connected=0

		try:
			self.cursor.close()
		except:pass
		try:
			self.cnx.close()
		except:pass

 

	def fetchOneAssoc(self,cursor) :

		data = cursor.fetchone()

		if data == None :
			return None

		desc = cursor.description

		dict = {}

		for (name, value) in zip(desc, data) :
			dict[name[0]] = value
		return dict

 

if __name__=="__main__":

	obj=myMysql()
	result=obj.mysqlConnect('localhost','usuario','pass','MiBaseDeDatos')

	if result:

		# ejemplo 1 - INSERT
		print obj.prepare("INSERT INTO tabla VALUES (null, now(), 'http')", None, False)
		print obj.lastId

		# ejemplo 2 - UPDATE
		query="UPDATE tabla SET Texto=%s WHERE id=%s"
		params=("XX",20)

		obj.prepare(query,params,False)

		if result:
			print result
		else:

			print obj.error

		print obj.affectedRows()

 
		# ejemplo 3 - SELECT
		result=obj.prepare("SELECT id,Texto FROM tabla WHERE id=%s", (20,))

		if result:
			print result
		else:
			print obj.error


		obj.mysqlClose()

	else:
		print obj.error 
