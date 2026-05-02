import sqlite3

conn = sqlite3.connect("safevault.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    Email TEXT
)
""")

cursor.execute("INSERT INTO Users (Username, Email) VALUES ('admin', 'admin@test.com')")

conn.commit()
conn.close()

print("DB creada correctamente")