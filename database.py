import sqlite3

conn = sqlite3.connect("anime.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS posted(
title TEXT
)
""")

conn.commit()

def is_posted(title):
    cur.execute("SELECT * FROM posted WHERE title=?", (title,))
    return cur.fetchone()

def save_post(title):
    cur.execute("INSERT INTO posted VALUES(?)", (title,))
    conn.commit()