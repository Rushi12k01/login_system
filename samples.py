import sqlite3
import hashlib

connection = sqlite3.connect("./projects/login_system/userdata.db")
current = connection.cursor()

current.execute("""
CREATE TABLE IF NOT EXISTS testdata (
    if INTEGER PRIMARY KEY,
    username VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL
)
""")

username1,password1 = 'rushi123',hashlib.sha512("bharti".encode()).hexdigest()
username2,password2 = 'golu213',hashlib.sha512("dimple".encode()).hexdigest()
username3,password3 = 'pooja',hashlib.sha512("sonu".encode()).hexdigest()
username4,password4 = 'rakka',hashlib.sha512("chintu".encode()).hexdigest()

current.execute("INSERT INTO testdata (username,password) VALUES (?,?)",(username1,password1))
current.execute("INSERT INTO testdata (username,password) VALUES (?,?)",(username2,password2))
current.execute("INSERT INTO testdata (username,password) VALUES (?,?)",(username3,password3))
current.execute("INSERT INTO testdata (username,password) VALUES (?,?)",(username4,password4))


connection.commit()

#commit
print("hello")

print("modified in new branch")