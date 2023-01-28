import sqlite3
import hashlib

connection = sqlite3.connect("userdata.sql")
cur = connection.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id integer primary key,
    username varchar(255) not null,
    password varchar(255) not null
)
""")

username1,password1= "rsk12",hashlib.sha256("12445".encode()).hexdigest()
cur.execute("insert into userdata (username,password) values (?,?)",(username1,password1))

connection.commit()