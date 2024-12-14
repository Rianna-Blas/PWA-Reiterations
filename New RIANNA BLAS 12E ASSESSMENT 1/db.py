import sqlite3
from werkzeug.security import generate_password

def GetDB():
    db = sqlite3.connect(".database/rookie.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllReviews():

db = GetDB()
reviews - db.execute("SELECT * FROM Guesses").fetchall()
db.close()
return reviews