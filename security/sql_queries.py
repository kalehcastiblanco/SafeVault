import sqlite3

def get_user_by_username(username):
    conn = sqlite3.connect("safevault.db")
    cursor = conn.cursor()

    query = "SELECT * FROM Users WHERE Username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchone()