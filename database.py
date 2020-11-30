import pymysql
import random


def openDB():
	try:
		connection =   pymysql.connect(host="10.0.1.21",user="Fria",passwd="Hej",database="project")
	except:
		print(">>\033[91m      Cant connect to db\033[0m")
		return False
	
	return connection


def closeDB(connection):
	#connection.close()
	return None

def send_stream():
	db = openDB()
	if db==False:
		return False
	try:
		with db.cursor() as cur:
			cur.execute("UPDATE imagetable SET image=LOAD_FILE('/homej/pi/stream.jpg') WHERE id='1'")

			db.commit()
	
	finally:
		closeDB(db)

def getDataForMail():
	result = []
	db = openDB()
	if db==False:
		return False
	try:
		with db.cursor() as cur:
			cur.execute("SELECT Email FROM users WHERE sendnotice = '1'")
			db.commit()
			rows = cur.fetchall()
		
		for row in rows:
			result.append(row[0])
	
	finally:
		closeDB(db)
		return result
	
	
def motion_detected():
	db = openDB()
	if db==False:
		return False
	try:
		with db.cursor() as cur:
			cur.execute("UPDATE systabell SET motionsensor = '1' WHERE id= '1'")
			db.commit()
	
	finally:
		print(">>  \033[92m20% printed to database\033[0m")
		closeDB(db)
	
	
def motion_detectedRESET():
	db = openDB()
	if db==False:
		return False
	try:
		with db.cursor() as cur:
			cur.execute("UPDATE systabell SET motionsensor = '0' WHERE id= '1'")
			db.commit()
	
	finally:
		print(">> \033[94m100% motion detection back online\033[0m")
		closeDB(db)
	

def camera_disconnected():
	db = openDB()
	if db==False:
		return False
	try:
		with db.cursor() as cur:
			cur.execute("UPDATE systabell SET camera = '0' WHERE id= '1'")
			db.commit()
	
	finally:
		print(">>\033[91m      Camera disconnected\033[0m")
		closeDB(db)
	
def camera_online():
	db = openDB()
	if db==False:
		return False
	try:
		with db.cursor() as cur:
			cur.execute("UPDATE systabell SET camera = '1' WHERE id= '1'")
			db.commit()
	
	finally:
		print(">>  \033[92mCamera Online\033[0m")
		closeDB(db)
	
def RASPI_online():
	db = openDB()
	if db==False:
		return False
	try:
		ping = random.random()
		with db.cursor() as cur:
			cur.execute("UPDATE systabell SET raspi = '%f' WHERE id= '1'" % ping)
			db.commit()
	
	finally:
		print(">>  \033[92mPi Online\033[0m")
		closeDB(db)
	

