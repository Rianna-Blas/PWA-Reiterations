
--Table for reviews--
CREATE TABLE Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, date TEXT NOT NULL, score INTEGER, review TEXT NOT NULL);

--Table for users database--
CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password NOT NULL);