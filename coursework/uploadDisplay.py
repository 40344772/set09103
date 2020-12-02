import sqlite3 as sql

def insertUpload(fileName,uploadDate):
        con = sql.connect("var/upload.db")
        cur = con.cursor()
        cur.execute("INSERT INTO upload_info (fileName,upload_date) VALUES (?,?)", (fileName,uploadDate))
        con.commit()
        con.close()

def display():
	con = sql.connect("var/upload.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM upload_info")
	data = cur.fetchall()
	con.close()
	return data
