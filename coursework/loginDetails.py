import sqlite3 as sql

def insertUser(username,password,accounttype):
	con = sql.connect("var/login.db")
	cur = con.cursor()
	cur.execute("INSERT INTO login_accounts (username,password,account_type) VALUES (?,?,?)", (username,password,accounttype))
	con.commit()
	con.close()

def userValidation(username,password):
	con = sql.connect("var/login.db")
	cur = con.cursor()
	cur.execute("""SELECT username, password FROM login_accounts WHERE username=? AND password=?""", (username, password))
	users = cur.fetchall()
	con.close()
	return users

def typeFind(username,password):
        con = sql.connect("var/login.db")
        cur = con.cursor()
        cur.execute("""SELECT account_type FROM login_accounts WHERE username=? AND password=?""", (username, password))
        typeCheck = cur.fetchall()
        con.close()
        return typeCheck

def getStud():
	con = sql.connect("var/login.db")
	cur = con.cursor()
	cur.execute("""SELECT account_type FROM login_accounts WHERE account_type='student' LIMIT 1""")
	stud = cur.fetchall()
	con.close()
	return stud
