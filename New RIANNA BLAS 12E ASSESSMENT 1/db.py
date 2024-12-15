import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():
    db = sqlite3.connect("database/username.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllReviews():
    db = GetDB()
    reviews = db.execute("""SELECT Reviews.date, Reviews.moviegame, Reviews.score, Users.username
                        FROM Reviews JOIN Users ON Reviews.user_id = Users.id 
                        ORDER BY date DESC""").fetchall()
    db.close()
    return reviews
    
def CheckLogin(username, password):

    db = GetDB()

    user = db.execute("SELECT * FROM Users WHERE usernsme=?", (username,)).fetchone()
    
    
    if user is not None:

        if check_password_hash(user['password'], password):

            return user

    return None

def RegisterUser(username, password):

    if username is None or password is None:
        return False
    
    db = GetDB()
    hash = generate_password_hash(password)
    db.execute("INSERT INTO Users(username, password) VALUES(?, ?)", (username, hash,))
    db.commit()

    return True

def AddReview(user_id, date, moviegame, score):

    if date is None or game is None:
        return False
    
    db = GetDB()
    db.execute("INSERT INTO Reviews(user_id, date, moviegame, score) VALUES(?, ?, ?, ?)", (user_id, date, moviegame, score))

    db.commit()

    return True

